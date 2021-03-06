#!/bin/bash

NOBS=rexloader
OPRJ=home:DarkSS
FPRJ=$OPRJ':fedora'
MPRJ=$OPRJ':mandriva'
DPRJ=$OPRJ':deb'
APRJ=$OPRJ':archlinux'
DSVN=~/Documents/obs/trash/$NOBS-0.1a.svn
DOBS=~/Documents/obs/home:DarkSS/$NOBS
DFBS=~/Documents/obs/home:DarkSS:fedora/$NOBS

echo -e '\e[0;4mChecking of google code version:\e[0m'
cd $DSVN
svn revert -q --recursive .
svn up
VSVN=`svnversion | grep -o '[0-9]*'`
echo -e '\nrevision #\e[0;33m'$VSVN'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'

VOBS=`osc ls -b $OPRJ $NOBS | grep -m 1 svn | awk -Fsvn. '{print $2}' | awk 'BEGIN {FS="[.,-]"} {print $1}'`
echo -e '\nrevision #\e[0;33m'$VOBS'\e[0m'

if [ $VSVN == $VOBS ]

then
  echo -e '\e[0;4m\nNo changes.\e[0m'

else
  svn log -r HEAD:$VOBS | less

  echo -e '\e[0;4m\nShould services be run?\e[0m'
  read

  for NPRJ in $OPRJ $FPRJ $DPRJ $APRJ

  do
    cd ~/Documents/obs/$NPRJ/$NOBS
    osc service rr
    osc up &
  done

fi

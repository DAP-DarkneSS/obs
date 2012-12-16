#!/bin/bash

NOBS=rexloader
OPRJ=home:DarkSS
FPRJ=$OPRJ':fedora'
MPRJ=$OPRJ':mandriva'
DPRJ=$OPRJ':deb'
DSVN=~/Documents/obs/trash/$NOBS
DOBS=~/Documents/obs/home:DarkSS/$NOBS
DMBS=~/Documents/obs/home:DarkSS:mandriva/$NOBS
DFBS=~/Documents/obs/home:DarkSS:fedora/$NOBS

echo -e '\e[0;4mChecking of google code version:\e[0m'
cd $DSVN
svn revert -q --recursive .
svn up
VSVN=`svnversion | grep -o '[0-9]*'`
echo -e '\nrevision #\e[0;33m'$VSVN'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'

VOBS=`osc ls -b $OPRJ $NOBS | tac | grep -m 1 svn | awk 'BEGIN {FS="[.,-]"} {print $6}'`
echo -e '\nrevision #\e[0;33m'$VOBS'\e[0m'

svn log | less

if [ $VSVN == $VOBS ]

then
  echo -e '\e[0;4m\nNo changes.\e[0m'

else

  echo -e '\e[0;4m\nShould services be run?\e[0m'
  read

  for NPRJ in $OPRJ $FPRJ $MPRJ $DPRJ

  do
    cd ~/Documents/obs/$NPRJ/$NOBS
    osc service rr
    osc up
  done

fi

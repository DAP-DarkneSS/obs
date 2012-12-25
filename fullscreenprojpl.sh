#!/bin/bash

NOBS=fullscreenprojpl
OPRJ=home:DarkSS
DPRJ=$OPRJ':deb'
DGIT=~/Documents/obs/trash/$NOBS

echo -e '\e[0;4mChecking of bitbucket version:\e[0m'
cd $DGIT
git pull
VGIT=`git log --date=raw -n1 | grep Date | awk '{print $2}'`
echo -e '\e[0;33m\n'$VGIT'\e[0m'

# echo -e '\e[0;4m\nChecking of OBS version:\e[0m'
# 
# VOBS=`osc ls -b $OPRJ $NOBS | tac | grep -m 1 svn | awk 'BEGIN {FS="[.,-]"} {print $6}'`
# echo -e '\nrevision #\e[0;33m'$VOBS'\e[0m'

git log --date=raw --full-diff --name-only

# if [ $VSVN == $VOBS ]

# then
#   echo -e '\e[0;4m\nNo changes.\e[0m'

# else

echo -e '\e[0;4m\nShould services be run?\e[0m'
read

for NPRJ in $OPRJ $DPRJ

do
  cd ~/Documents/obs/$NPRJ/$NOBS
  osc service rr
  osc up
done

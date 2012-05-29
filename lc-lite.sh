#!/bin/bash

NOBS=leechcraft
DGIT=~/lc/$NOBS
NPRJ=home:Reki:leechcraft:masterbranch
SPEC='https://api.opensuse.org:443/public/source/'$NPRJ'/'$NOBS'/'$NOBS'.spec'
MONI='https://api.opensuse.org:443/public/build/'$NPRJ'/_result'

echo -e '\e[0;4mChecking of github version:\e[0m'
cd $DGIT
git pull
VGIT=`git describe`
echo -e '\e[0;33m\n'$VGIT'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'

VOBS=`curl -s $SPEC | grep 'define LEECHCRAFT' | awk '{print $3}'`
echo -e '\e[0;33m\n'$VOBS'\e[0m'

echo -e '\e[0;4m\nChecking of OBS status:\n\e[0m'
curl -s curl -s $MONI | tr '"' ' ' | grep $NOBS | awk '{print $5 "\t" $7}'

if [ "$VGIT" == "$VOBS" ]

then
  echo -e '\e[0;4m\nNo changes.\e[0m'

else
  echo -e '\e[0;35m\nThe spec could be edited!\e[0m'

fi
#!/bin/bash

NOBS=leechcraft
DGIT=~/Documents/obs/trash/$NOBS-git
DOBS=~/Documents/obs/home:Reki:leechcraft:masterbranch/$NOBS

echo -e '\e[0;4mChecking of github version:\e[0m'
cd $DGIT
git pull
VGIT=`git describe origin/master`
echo -e '\e[0;33m\n'$VGIT'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'
cd $DOBS
osc up
VOBS=`grep 'define LEECHCRAFT' $NOBS.spec | awk '{ print $3 }'`
echo -e '\e[0;33m\n'$VOBS'\e[0m'

echo -e '\e[0;4m\nChecking of OBS status:\e[0m'
osc pr -n $NOBS | grep openSUSE

if [ "$VGIT" == "$VOBS" ]

then
  echo -e '\e[0;4m\nNo changes.\e[0m'

else

  cd $DGIT
  git log $VOBS..HEAD --date=raw --full-diff --name-only
  cd $DOBS

  echo -e '\e[0;4m\nShould the spec be edited?\e[0m'
  read

  CTIME=`date +%g'.'%m'.'%d'-'%H.%M.%S`
  cp ./$NOBS.spec ./$NOBS.spec.$VOBS.$CTIME
  sed "s/$VOBS/$VGIT/g" ./$NOBS.spec.$VOBS.$CTIME > ./$NOBS.spec

  echo -e '\e[0;4m\nShould the commit be done?\e[0m'
  read
  osc ci -m $VGIT

  echo -e '\e[0;4m\nGit will be updated...\e[0m'
  cd ../..
  git commit $DOBS -m 'LeechCraft '$VGIT'.'
  kdialog --title "SSH" --passivepopup "Enter passphrase for key!"
  git push -u origin master

fi

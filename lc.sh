#!/bin/bash

REPO=home:Reki:leechcraft:masterbranch
NOBS=leechcraft
DGIT=~/Documents/obs/trash/$NOBS-git
DOBS=~/Documents/obs/home:Reki:leechcraft:masterbranch/$NOBS

echo -e '\e[0;4mChecking of github version:\e[0m'
cd $DGIT
git reset --hard origin
git pull --all
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
  git diff $VOBS..HEAD --name-status | grep "^A" | less
  cd $DOBS

  echo -e '\e[0;4m\nShould the spec be edited?\e[0m'
  read

  CTIME=`date +%g'.'%m'.'%d'-'%H.%M.%S`
  cp ./$NOBS.spec ./$NOBS.spec.$VOBS.$CTIME
  cp ./$NOBS-doc.spec ./$NOBS-doc.spec.$VOBS.$CTIME
  sed "s/$VOBS/$VGIT/g" ./$NOBS.spec.$VOBS.$CTIME > ./$NOBS.spec
  sed "s/$VOBS/$VGIT/g" ./$NOBS-doc.spec.$VOBS.$CTIME > ./$NOBS-doc.spec
  rm $NOBS*.spec.$VOBS.$CTIME

  echo -e '\e[0;4m\nShould the commit be done?\e[0m'
  read
  osc ci -m $VGIT &
  osc service rr $REPO $NOBS-doc &

  echo -e '\e[0;4m\nGit will be updated...\e[0m'
  cd ../..
  git commit $DOBS -m 'LeechCraft '$VGIT'.'
  kdialog --title "SSH" --passivepopup "Enter passphrase for key!"
  git push -u origin master

fi

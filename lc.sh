#!/bin/sh

DGIT=~/Documents/obs/trash/leechcraft
DOBS=~/Documents/obs/home:Reki:leechcraft:masterbranch/leechcraft

echo 'Checking of github version:'
cd $DGIT
git pull
VGIT=`git describe`
echo -e '\n'$VGIT

echo -e '\nChecking of OBS version:'
cd $DOBS
osc up
VOBS=`grep 'define LEECHCRAFT' leechcraft.spec | awk '{ print $3 }'`
echo -e '\n'$VOBS

echo -e '\nChecking of OBS status:'
osc pr -n leechcraft | grep openSUSE

if [ $VGIT == $VOBS ]

then
  echo -e '\nNo changes.'

else

  echo -e '\nShould the spec be edited?'
  read

  CTIME=`date +%s`
  cp ./leechcraft.spec ./leechcraft.spec.$VOBS.$CTIME
  sed "s/$VOBS/$VGIT/g" ./leechcraft.spec.$VOBS.$CTIME > ./leechcraft.spec

  echo -e '\nShould the commit be done?'
  read
  osc ci -m $VGIT

fi
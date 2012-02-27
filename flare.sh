#!/bin/sh

DGIT=~/Documents/obs/trash/flare
DOBS=~/Documents/obs/home:DarkSS/flare

echo 'Checking of github version:'
cd $DGIT
git pull
VGIT=`git describe`
echo -e '\n'$VGIT
echo 'Unix timestamp: '`git log -n 1 --date=raw | grep Date | awk '{ print $2 }'`

echo -e '\nChecking of OBS version:'
cd $DOBS
osc up
VOBS=`grep Timestamp flare.spec -m 1 | awk '{ print $9 }' | sed 's/.$//'`
echo -e '\n'$VOBS
echo 'Unix timestamp: '`grep Timestamp flare.spec -m 1 | awk '{ print $6 }' | sed 's/.$//'`

if [ $VGIT == $VOBS ]

then
  echo -e '\nNo changes.'

else

  echo -e '\nWould the spec be edited?'
  read

  cp ./leechcraft.spec ./leechcraft.spec.$VOBS.`date +%s`

  echo -e '\nShould the commit be done?'
  read
  osc ci -m $VGIT

fi
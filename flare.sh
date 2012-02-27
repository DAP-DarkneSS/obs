#!/bin/sh

DGIT=~/Documents/obs/trash/flare
DOBS=~/Documents/obs/home:DarkSS/flare

echo 'Checking of github version:'
cd $DGIT
git pull
VGIT=`git describe`
TGIT=`git log -n 1 --date=raw | grep Date | awk '{ print $2 }'`
echo -e '\n'$VGIT
echo 'Unix timestamp: '$TGIT

echo -e '\nChecking of OBS version:'
cd $DOBS
osc up
XOBS=`grep Timestamp flare.spec -m 1`
VOBS=`echo $XOBS | awk '{ print $9 }' | sed 's/.$//'`
TOBS=`echo $XOBS | awk '{ print $6 }' | sed 's/.$//'`
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

#echo -e '\n'`LANG=en_GB.UTF-8 date +'* '%a' '%b' '%d' '%Y' DA <dap.darkness@gmail.com> - '%Y%m%d'-1'`'\n- Version 0.15 alfa. Timestamp: 1329962944. Git describe: v0.14-516-g8333245.\n\n'
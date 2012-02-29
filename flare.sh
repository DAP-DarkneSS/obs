#!/bin/sh

NOBS=flare
DGIT=~/Documents/obs/trash/$NOBS
DOBS=~/Documents/obs/home:DarkSS/$NOBS

echo -e '\e[0;4mChecking of github version:\e[0m'
cd $DGIT
git pull
VGIT=`git describe`
TGIT=`git log -n 1 --date=raw | grep Date | awk '{ print $2 }'`
echo -e '\e[0;33m\n'$VGIT'; unix timestamp: '$TGIT'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'
cd $DOBS
osc up
XOBS=`grep Timestamp $NOBS.spec -m 1`
VOBS=`echo $XOBS | awk '{ print $9 }' | sed 's/.$//'`
TOBS=`echo $XOBS | awk '{ print $6 }' | sed 's/.$//'`
echo -e '\e[0;33m\n'$VOBS'; unix timestamp: '$TOBS'\e[0m'

if [ $VGIT == $VOBS ]

then
  echo -e '\e[0;4m\nNo changes.\e[0m'

else

  echo -e '\e[0;4m\nShould the spec be edited?\e[0m'
  read

  CTIME=`date +%g'.'%m'.'%d'-'%H.%M.%S`
  cp ./$NOBS.spec ./$NOBS.spec.$VOBS.$CTIME
  YOBS='\n'`LANG=en_GB.UTF-8 date +'* '%a' '%b' '%d' '%Y' DA <dap.darkness@gmail.com> - '%Y%m%d'-1'`'\n- Version 0.15 alfa. Timestamp: '$TGIT'. Git describe: '$VGIT'.\n'
  sed "s/changelog$/&$YOBS/g" ./$NOBS.spec.$VOBS.$CTIME > ./$NOBS.spec

  echo -e '\e[0;4m\nShould the commit be done?\e[0m'
  read
  osc ci -m $VGIT

  echo -e '\e[0;4m\nGit will be updated...\e[0m'
  cd ../..
  git commit -a -m 'Flare '$VGIT'.'
  git push -u origin master

fi
#!/bin/zsh

NOBS=rexloader
DSVN=~/Documents/obs/trash/$NOBS
DOBS=~/Documents/obs/home:DarkSS/$NOBS
DMBS=~/Documents/obs/home:DarkSS:mandriva/$NOBS

echo -e '\e[0;4mChecking of google code version:\e[0m'
cd $DSVN
svn up
VSVN=`svnversion | grep -o '[0-9]*'`
echo -e '\nrevision #\e[0;33m'$VSVN'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'
cd $DOBS
osc up
VOBS=`grep Revision $NOBS.spec -m 1 | grep -o '[0-9]*'`
echo -e '\nrevision #\e[0;33m'$VOBS'\e[0m'

if [ $VSVN == $VOBS ]

then
  echo -e '\e[0;4m\nNo changes.\e[0m'

else

  echo -e '\e[0;4m\nShould the spec be edited?\e[0m'
  read

  CTIME=`date +%g'.'%m'.'%d'-'%H.%M.%S`

  function spec {
  cp ./$NOBS.spec ./$NOBS.spec.$VOBS.$CTIME
  YOBS='\n'`LANG=en_GB.UTF-8 date +'* '%a' '%b' '%d' '%Y' DA <dap.darkness@gmail.com> - '%Y%m%d'-1'`'\n- Revision #'$VSVN'.\n'
  sed "s/changelog$/&$YOBS/g" ./$NOBS.spec.$VOBS.$CTIME > ./$NOBS.spec
  }

  spec

  cd $DMBS
  osc up
  spec

  echo -e '\e[0;4m\nShould the commit be done?\e[0m'
  read
  osc ci -m 'Revision #'$VSVN'.'

  cd $DOBS
  osc ci -m 'Revision #'$VSVN'.'

  echo -e '\e[0;4m\nGit will be updated...\e[0m'
  cd ../..
  git commit -a -m 'Rexloader rev'$VSVN'.'
  kdialog --title "SSH" --passivepopup "Enter passphrase for key!"
  git push -u origin master

fi
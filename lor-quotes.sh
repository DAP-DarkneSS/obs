#!/bin/zsh

NOBS=fortunes-lor-quotes
DOBS=~/Documents/obs/home:DarkSS/lor-quotes

echo -e '\e[0;4mChecking of google code version:\e[0m'
VDAT=`LANG=en_GB.UTF-8 date +%Y%m%d`
echo -e '\ntoday is \e[0;33m'$VDAT'\e[0m'

echo -e '\e[0;4m\nChecking of OBS version:\e[0m'
cd $DOBS
osc up
VOBS=`grep Date $NOBS.spec -m 1 | grep -o '[0-9]*'`
echo -e '\nthe last update was \e[0;33m'$VOBS'\e[0m'

if [ $VDAT == $VOBS ]

then
  echo -e '\e[0;4m\nThe last update was today.\e[0m'

else

  echo -e '\e[0;4m\nShould the spec & service be edited?\e[0m'
  read

  CTIME=`date +%H.%M.%S`
  cp ./$NOBS.spec ./$NOBS.spec.$VDAT-$CTIME
  YOBS='\n'`LANG=en_GB.UTF-8 date +'* '%a' '%b' '%d' '%Y' DA <dap.darkness@gmail.com> - '%Y%m%d'-1'`'\n- Date '$VDAT'.\n'
  sed "s/changelog$/&$YOBS/g" ./$NOBS.spec.$VDAT-$CTIME > ./$NOBS.spec.tmp
  sed "s/date $VOBS/date $VDAT/g" ./$NOBS.spec.tmp > ./$NOBS.spec
  rm ./$NOBS.spec.tmp

  cp ./_service ./_service.$VDAT-$CTIME
  sed "s/$VOBS/$VDAT/g" ./_service.$VDAT-$CTIME > ./_service

  echo -e '\e[0;4m\nShould the commit be done?\e[0m'
  read
  osc ci -m 'Date '$VDAT'.'

  echo -e '\e[0;4m\nGit will be updated...\e[0m'
  cd ../..
  git commit -a -m 'Fortunes LOR quotes, update date: '$VDAT'.'
  git push -u origin master

fi
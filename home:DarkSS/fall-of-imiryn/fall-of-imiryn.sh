#!/bin/sh -e

if [ ! -d $HOME/.fall-of-imiryn ] ; then
	mkdir $HOME/.fall-of-imiryn
	cp -a /usr/share/fall-of-imiryn/save $HOME/.fall-of-imiryn/
fi

cd /usr/share/fall-of-imiryn
python2 main.py

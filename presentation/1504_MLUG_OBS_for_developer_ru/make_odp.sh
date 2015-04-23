#!/bin/bash

NAME=`pwd | awk -F / '{print $NF}'`

zip -r -9 $NAME.odp *.xml mimetype Pictures Thumbnails
xdg-open $NAME.odp
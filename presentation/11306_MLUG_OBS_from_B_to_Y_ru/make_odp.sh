#!/bin/bash

NAME=OBS_from_B_to_Y

zip -r -9 $NAME.odp *.xml mimetype Pictures Thumbnails
xdg-open $NAME.odp
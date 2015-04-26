#!/bin/bash
#
# pdnsd sleep script for systemd
#
# Dmitriy Perlow <dap.darkness@gmail.com>
#

if [ "$1" = pre ]

then
  /bin/systemctl stop pdnsd.service
fi

if [ "$1" = post ]

then
  /usr/bin/sleep 1
  /bin/systemctl start pdnsd.service
fi

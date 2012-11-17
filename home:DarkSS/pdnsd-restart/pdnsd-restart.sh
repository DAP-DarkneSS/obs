#! /bin/sh
#
# pdnsd dispatcher script for NetworkManager
#
# Dmitriy Perlow <dap.darkness@gmail.com>
#
if test -x /bin/systemctl && /bin/systemctl -q is-enabled pdnsd.service

then
  /bin/systemctl restart pdnsd.service

fi
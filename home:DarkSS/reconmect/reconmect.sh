#! /bin/bash
#
#=================================|Copying|=================================#
#
# RecoNMect is a tool to restart Network Manager active connection
# if there are no access to both of selected servers.
# Copyright (C) 2013 Dmitriy A. Perlow <dap.darkness@gmail.com>
#
# This file is part of RecoNMect.
#
# RecoNMect is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
#
# RecoNMect is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with RecoNMect.  If not, see
# <http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>.
#
# You could contact me with e-mail or jabber dap.darkness@gmail.com
#
#==================================|Source|=================================#

CHECKME1="8.8.4.4"
CHECKME2="84.201.225.101"
SLEEP="11"
FPING="/usr/sbin/fping"
LOG="/tmp/reconmect.log"
LIFE="SENSE"

echo `date`" Hi!" | tee -a $LOG

while test $LIFE

do
  sleep $SLEEP

  if $FPING $CHECKME1 && $FPING $CHECKME2

  then
    echo `date`" ok!" | tee -a $LOG

  else
    echo `date`" Bye!" | tee -a $LOG
    LIFE=""
    /bin/systemctl restart NetworkManager.service

  fi

done
# mini-snmpd-nagios-plugins

Nagios/centreon plugins for [mini-snmpd](https://github.com/troglobit/mini-snmpd) server.

## Overview

Plugin scope :

- [x] disk
- [] load
- [] uptime
- [] ram
- [] cpu ?

## Disk 

Exemple :

'''sh
$ get_disk_value.py -H hostname -C community
OK- / est à 51%.|/storage/log=3617952;;;0;7224824
'''

full documentation :

'''sh
python get_disk_value.py  -h
usage: get_disk_value.py [-h] -H [HOSTNAME] [-C [COMMUNITY]] [-P [PORT]]
                         [-D [DISK]] [-w [WARNING]] [-c [CRITICAL]]

Monitor disk on mini-snmpd server.

optional arguments:
  -h, --help            show this help message and exit
  -H [HOSTNAME], --hostname [HOSTNAME]
                        Hostname
  -C [COMMUNITY], --community [COMMUNITY]
                        SNMP Community
  -P [PORT], --port [PORT]
                        SNMP Port
  -D [DISK], --disk [DISK]
                        Disk Number
  -w [WARNING], --warning [WARNING]
                        Warning treshold
  -c [CRITICAL], --critical [CRITICAL]
                        Critical treshold
'''

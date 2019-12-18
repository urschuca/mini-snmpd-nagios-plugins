# mini-snmpd-nagios-plugins

Nagios/centreon plugins for [mini-snmpd](https://github.com/troglobit/mini-snmpd) server.

## Overview

Plugin scope :

- [x] disk
- [x] load
- [ ] ram
- [ ] cpu ?

## Disk 

Exemple :

```
$ get_disk_value.py -H hostname -C community
OK- / est à 51%.|/storage/log=3617952;;;0;7224824
```

Documentation :

```
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
```

## Load

Exemple :

```
 python get_load.py -H hostname -C community
OK: Load average:3.63, 3.56, 3.60|Load1=3.63;10.0;20.0;; Load5=3.56;10.0;20.0;; Load15=3.60;10.0;20.0;;
```

Documentation :

```
python get_load.py -h
usage: get_load.py [-h] -H [HOSTNAME] [-C [COMMUNITY]] [-P [PORT]]
                   [-w [WARNING]] [-c [CRITICAL]]

Get load 1,5,15 on mini-snmpd server.

optional arguments:
  -h, --help            show this help message and exit
  -H [HOSTNAME], --hostname [HOSTNAME]
                        Hostname
  -C [COMMUNITY], --community [COMMUNITY]
                        SNMP Community
  -P [PORT], --port [PORT]
                        SNMP Port
  -w [WARNING], --warning [WARNING]
                        Warning treshold
  -c [CRITICAL], --critical [CRITICAL]
                        Critical treshold
```

#!/usr/bin/python
# coding: utf-8
import argparse
from pysnmp.hlapi import *

# Exit statuses recognized by Nagios
UNKNOWN = -1
OK = 0
WARNING = 1
CRITICAL = 2

# Valide argument
parser = argparse.ArgumentParser(description='Monitor disk on mini-snmpd server.')
parser.add_argument('-H', '--hostname', type=str, nargs='?', required=True, help='Hostname')
parser.add_argument('-C', '--community', type=str, nargs='?', help='SNMP Community', default='public')
parser.add_argument('-P', '--port', type=str, nargs='?', help='SNMP Port', default='161')
parser.add_argument('-D', '--disk', type=int, nargs='?', help='Disk Number', default='1')
parser.add_argument('-w', '--warning', type=int, nargs='?', help='Warning treshold', default='80')
parser.add_argument('-c', '--critical', type=int, nargs='?', help='Critical treshold', default='90')

args = parser.parse_args()

# monitor

data = (
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'dskPath', args.disk)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'dskTotal', args.disk)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'dskAvail', args.disk)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'dskUsed', args.disk)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'dskPercent', args.disk))
)

g = getCmd(SnmpEngine()
           , CommunityData(args.community, mpModel=1)
           , UdpTransportTarget((args.hostname, args.port))
           , ContextData()
           , *data)

errorIndication, errorStatus, errorIndex, varBinds = next(g)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (
                         errorStatus.prettyPrint(),
                         errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
                       )

          )

else:
    Name = str(varBinds[0]).split('= ')[1]
    Total = str(varBinds[1]).split('= ')[1]
    Used = str(varBinds[3]).split('= ')[1]
    Percent = int(str(varBinds[4]).split('= ')[1])
    
    perfdata= "- "+Name+" est à "+str(Percent)+"%.|"+Name+"="+Used+";;;0;"+Total+""
	
    if Percent >= args.critical:
        print("Critical"+perfdata)
        exit(CRITICAL)
    elif  Percent >= args.warning:
        print("Warning"+perfdata)
        exit(WARNING)
    else:
        print("OK"+perfdata)
        exit(OK)


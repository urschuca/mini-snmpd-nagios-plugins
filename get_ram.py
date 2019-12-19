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
parser = argparse.ArgumentParser(description='Monitor RAM on mini-snmpd server.')
parser.add_argument('-H', '--hostname', type=str, nargs='?', required=True, help='Hostname')
parser.add_argument('-C', '--community', type=str, nargs='?', help='SNMP Community', default='public')
parser.add_argument('-P', '--port', type=int, nargs='?', help='SNMP Port', default='161')
parser.add_argument('-w', '--warning', type=float, nargs='?', help='Warning treshold', default='80')
parser.add_argument('-c', '--critical', type=float, nargs='?', help='Critical treshold', default='90')

args = parser.parse_args()

# monitor

data = (
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memTotalReal', 0)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memAvailReal', 0)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memShared', 0)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memBuffer', 0)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memCached', 0))
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

    Total= str(varBinds[0]).split('= ')[1]
    Avail= str(varBinds[1]).split('= ')[1]
    Shared= str(varBinds[2]).split('= ')[1]
    Buffer= str(varBinds[3]).split('= ')[1]
    Cached= str(varBinds[4]).split('= ')[1]

    int_total=int(Total)
    int_avail=int(Avail)
    int_shared=int(Shared)
    int_buffer=int(Buffer)
    int_cached=int(Cached)

#   perfdata= "- "+Name+" est à "+str(Percent)+"%.|"+Name+"="+Used+";;;0;"+Total+""
#	
#    if Percent >= args.critical:
#        print("Critical"+perfdata)
#        exit(CRITICAL)
#    elif  Percent >= args.warning:
#        print("Warning"+perfdata)
#        exit(WARNING)
#    else:
#        print("OK"+perfdata)
#        exit(OK)


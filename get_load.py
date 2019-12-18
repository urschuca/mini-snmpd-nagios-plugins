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
parser = argparse.ArgumentParser(description='Get uptime on mini-snmpd server.')
parser.add_argument('-H', '--hostname', type=str, nargs='?', required=True, help='Hostname')
parser.add_argument('-C', '--community', type=str, nargs='?', help='SNMP Community', default='public')
parser.add_argument('-P', '--port', type=str, nargs='?', help='SNMP Port', default='161')
parser.add_argument('-w', '--warning', type=float, nargs='?', help='Warning treshold', default='10')
parser.add_argument('-c', '--critical', type=float, nargs='?', help='Critical treshold', default='20')

args = parser.parse_args()

# monitor

data = (
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'laLoad', 1)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'laLoad', 2)),
  ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'laLoad', 3))
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
    
    Loada=str(varBinds[0]).split('= ')[1]
    Loadb=str(varBinds[1]).split('= ')[1]
    Loadc=str(varBinds[2]).split('= ')[1]

    perfdata= ": Load average:"+Loada+", "+Loadb+", "+Loadc+"|Load1="+Loada+";"+str(args.warning)+";"+str(args.critical)+";; Load5="+Loadb+";"+str(args.warning)+";"+str(args.critical)+";; Load15="+Loadc+";"+str(args.warning)+";"+str(args.critical)+";; "

    fl_load=float(Loada)
	
    if fl_load >= args.critical:
        print("Critical"+perfdata)
        exit(CRITICAL)
    elif  fl_load >= args.warning:
        print("Warning"+perfdata)
        exit(WARNING)
    else:
        print("OK"+perfdata)
        exit(OK)


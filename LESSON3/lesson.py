#!/usr/bin/env python
import snmp_helper
if True:
    IP = '184.105.247.70'
    IP2 = '184.105.247.71'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 161)
    pynet_rtr2 = (IP2, 161)
snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.1.5.0')
output = snmp_helper.snmp_extract(snmp_data)
print output

#!/usr/bin/env python

#netmiko made by Kirk
from netmiko import ConnectHandler
from getpass import getpass
password = '88newclass'

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
    }
pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    }

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
    'secret': '',
    }


# ** = passes the dictionary as arguments to the Connect Handler = key:value pairs
pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

devices = [ pynet_rtr1, pynet_rtr2, srx ]

for i in devices:
    outp = i.send_command("show arp")
    print outp



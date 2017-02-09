#!/usr/bin/env python

#netmiko made by Kirk
from netmiko import ConnectHandler
from getpass import getpass
password = '88newclass'

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    }

# ** = passes the dictionary as arguments to the Connect Handler = key:value pairs
pynet_rtr2 = ConnectHandler(**pynet2)

#CONFIG MODE
pynet_rtr2.config_mode()
print pynet_rtr2.check_config_mode()



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
print dir(pynet_rtr1)
print pynet_rtr1.find_prompt()
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

#display the prompt if we obtained it
print srx.find_prompt()

#CONFIG MODE
#pynet_rtr1.config_mode()
#print pynet_rtr1.check_config_mode()

#this lib adds automaticaly \n + strips
print "before send command"
outp = pynet_rtr1.send_command("show ip int brief")
print outp
print "after send command and print outp"

#paging is automatically disabled
outp = pynet_rtr1.send_command("show version")
print outp
print "after show version"

#command array
config_commands = ['logging buffered 19999']
output = pynet_rtr1.send_config_set(config_commands)
print output

#JUNIPER
print "JUNIPER"
outp = srx.send_command("show arp")
print outp

#srx.config_mode()
#srx.check_config_mode()

config_commands = ['set system host-name gigel']
outp = srx.send_config_set(config_commands)
srx.commit()


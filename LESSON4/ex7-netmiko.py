#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    '''
    Use Netmiko to change the logging buffer size and to disable console logging
    from a file for both pynet-rtr1 and pynet-rtr2
    '''
    password = '88newclass'

    # Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password

    for a_device in (pynet1, pynet2):
        net_connect = ConnectHandler(**a_device)
        net_connect.send_config_from_file(config_file='config_file.txt')

        # Verify configuration
        output = net_connect.send_command("show run | inc logging")
        print
        print '#' * 80
        print "Device: {}:{}".format(net_connect.ip, net_connect.port)
        print
        print output
        print '#' * 80
        print

if __name__ == "__main__":
    main()

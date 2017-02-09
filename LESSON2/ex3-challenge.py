#!/usr/bin/env python

import telnetlib
import time
import socket
import sys
import getpass

class beammeup:

    def __init__(self, PORT, TIMEOUT,IP, username, password):
        self.PORT = PORT
        self.TIMEOUT = TIMEOUT
        self.IP = IP
        self.username = username
        self.password = password
        self.description = "Connects to a device and does sh ip int brief"
        self.remote_conn = self.telnet_connect(self.IP, self.PORT, self.TIMEOUT)        
        
    def send_command(self, cmd):
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()

    def login(self):
    
        output = self.remote_conn.read_until("sername:", self.TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", self.TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        time.sleep(1)
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
          Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(paging_cmd)

    def telnet_connect(self, ip_addr, TELNET_PORT, TELNET_TIMEOUT):
        '''
        Establish telnet connection
        '''
        try:
             return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

    def close_conn(self):
        self.remote_conn.close()


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()

#getpass.getpass()
# 11     def __init__(self, PORT, TIMEOUT,IP, username, password):
    my_conn = beammeup(23, 6, ip_addr, 'pyclass', '88newclass') 
    my_conn.login()
    my_conn.disable_paging()
    output = my_conn.send_command('show ip int brief')
    print "gogu" + output
    my_conn.close_conn()

if __name__ == "__main__":
    main()

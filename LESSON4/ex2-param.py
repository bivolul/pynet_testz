#!/usr/bin/env python
'''
show version
'''

import paramiko
import time
from getpass import getpass
import re

def read_buf(remote_conn):
    if remote_conn.recv_ready():
        return remote_conn.recv(65535)

def main():
    
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass()
    port = 22

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()

    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password,look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    time.sleep(2)
    read_buf(remote_conn)
    remote_conn.send("conf t\n")
    time.sleep(2)
    outp = read_buf(remote_conn)
    #pynet-rtr2(config)#
    print outp
    remote_conn.send("logging buffered 19999\n")
    time.sleep(2)
    outp = read_buf(remote_conn)
    print outp
if __name__ == "__main__":
    main()

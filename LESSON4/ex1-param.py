#!/usr/bin/env python
'''
show version
'''

import paramiko
import time
from getpass import getpass

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

    time.sleep(5)
    read_buf(remote_conn)
    remote_conn.send("terminal length 0\n")
    time.sleep(5)
    read_buf(remote_conn)

    remote_conn.send("show version\n")
    time.sleep(2)
    output=read_buf(remote_conn)
    print output
    print '\n Finished'

if __name__ == "__main__":
    main()

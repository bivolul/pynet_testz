#!/usr/bin/env python

import paramiko
from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
#88newclass
password = getpass()
port = 22

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
#DEBUG - print remote_conn_pre
#needed to start a shell in order to send commands
remote_conn = remote_conn_pre.invoke_shell()
#5k
outp = remote_conn.recv(5000)
print outp

remote_conn.send('show users\n')
oo = remote_conn.recv(5000)
print oo

#how many bytes I will read from what came back over the socket
#outp = remote_conn.recv(5000)
#print outp

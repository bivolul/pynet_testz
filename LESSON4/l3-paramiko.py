#!/usr/bin/env python

import paramiko
#from getpass import getpass
import time

ip_addr = '184.105.247.71'
username = 'pyclass'
#88newclass
password = '88newclass'
port = 22

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#if no need to accept the public key of the device, as it exists already in known_hosts, then load content of
#known_hosts into here
remote_conn_pre.load_system_host_keys()
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
#stdin, stdout, stderr = remote_conn_pre.exec_command('show ip int brief\n')
#print stdout.read()
# EXEC COMMAND = SSH COMMAND => AFTER ONE COMMAND, IT CLOSES THE SSH CONNECTION AND IT NEEDS REINIT
# FOR OTHER PURPOSES OR WITH NETWORK DEVICES, IT IS BETTER TO OPEN A SHELL
#RECONNECT AS EXEC DISCONNECTS AND DOES NOT MAKE A SESSION LIKE THIS ONE BELOW WITH SHELL
#remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
remote_conn = remote_conn_pre.invoke_shell()
time.sleep(5)
#print remote_conn.recv_ready()
remote_conn.settimeout(60.0)
#remote_conn.gettimeout()

#IS DATA AVAILABLE TO READ? => then read ..use an IF
#remote_conn.recv_ready()
outp = remote_conn.send("\n")
outp = remote_conn.recv(5000)
print outp

remote_conn.send("terminal length\n")
outp = remote_conn.recv(65535)
print outp
print "before show run"
outp = remote_conn.send("show ip int brief\n")
outp = remote_conn.recv(65535)
print outp
 

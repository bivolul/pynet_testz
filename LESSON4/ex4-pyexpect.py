#!/usr/bin/env python

import sys
import pexpect
import time
import re
from getpass import getpass

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22
    password = '88newclass'

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')

    ssh_conn.sendline('')
    ssh_conn.expect('#')
#show also the command typed, otherwise if only the output, then ssh_conn.after
# or just use the sys.stdout and ssh_conn.logfile
    print ssh_conn.before
    
    ssh_conn.sendline('conf t')
    ssh_conn.expect('config')
    ssh_conn.sendline('logging buffered 20010')
    ssh_conn.expect('config')
    
    ssh_conn.sendline('do sh run | i logg')
    ssh_conn.expect('config')
    print ssh_conn.after

if __name__ == "__main__":
    main()


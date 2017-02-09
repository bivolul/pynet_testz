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

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('#')
#show also the command typed, otherwise if only the output, then ssh_conn.after
# or just use the sys.stdout and ssh_conn.logfile
    print ssh_conn.before
    
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('#')
    ssh_conn.sendline('sh run')
    ssh_conn.expect('#')

    try:
        ssh_conn.sendline('show version')
        ssh_conn.expect('zzzzz')
    except pexpect.TIMEOUT:
        print 'Found timeout'

#^ matches the position immediately following a newline and $ matches the position immediately preceding a newline.

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    print "AFTER MATCH RE"
    print ssh_conn.after

if __name__ == "__main__":
    main()


#!/usr/bin/env python
import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Oh dear, the socket timed out..")
 
def send_command(remote_conn, cmd):
    #remove new line (1 character end trailing from the right)
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def login(remote_conn, username, password):
    #todo - more robust, try a few times before giving up
     output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
     remote_conn.write(username + '\n')
     output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
     remote_conn.write(password + '\n')    
     return output

def main():
    ip_addr = "184.105.247.70"
    username = "pyclass"
    password = "88newclass"

    remote_conn = telnet_connect(ip_addr)

    output = login(remote_conn,username,password)
    time.sleep(1)

    output = send_command(remote_conn, 'terminal length 0')
    output = send_command(remote_conn, 'show ip int brief')
    print output
    
    remote_conn.close()
if __name__ == "__main__":
    main()

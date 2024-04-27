'''socket programming in python'''
import socket
import sys
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.google.com')
print(ip)
'''


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket succefully created!')
except socket.error as err:
    print(f'socket creation failed with error {err}') 
      
port = 80

try :
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('error resolving the host')
    sys.exit()
s.connect((host_ip, port))
print(f'socket has succesfully connected to github on port == {host_ip}')


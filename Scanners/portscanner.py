#!/usr/bin/env python3

# PortScanner for Pen-Testing
# CyberSamurai DK
# Test this script on scanme.nmap.org to see how it functions

import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[ ಠ_ಠ SCANNING TARGET  ===> ] ' + str(target))
    for port in range(1, 500):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(sock):
    return sock.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)  # scanner quality depends on time spent
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port: ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port: ' + str(port) + ' : No banner :( ')
    except:
        # print('[-] Port: ' + str(port) + ' Is Closed')
        pass


targets = input('[!] Enter Target/s To Scan(Seperate multiple targets with comma): ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)

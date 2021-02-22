#!/usr/bin/env python3

# SPIDER
# Will crawl through websites and make clickable links!
# syntax: https://website.com
# CyberSamurai DK

import requests
import re
import urllib.parse as urlparse

target_url = input('[!] (⌐■_■) Enter a target URL: ')
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))   # Pytex And Regex here, also famous Byte to a string solution


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)

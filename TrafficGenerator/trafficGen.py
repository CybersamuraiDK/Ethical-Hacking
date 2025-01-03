#!/usr/bin/env python3
#Usage: python3 trafficGEN.py --file urls.txt --min_requests 10 --max_requests 50 --proxy http://username:password@proxyserver:port
import requests
import time
import random
import logging
import argparse
from concurrent.futures import ThreadPoolExecutor

# Logging configuration
logging.basicConfig(
    filename='traffic_generator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
]

def load_urls_from_file(filename):
    """Load URLs from a file."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        exit(1)

def send_request(url, proxy=None):
    """Send a single HTTP GET request to the specified URL."""
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
        logging.info(f"Request to {url} returned status code {response.status_code}")
    except requests.exceptions.Timeout:
        logging.warning(f"Request to {url} timed out.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request to {url} failed: {e}")

def generate_traffic(url, num_requests, proxy=None):
    """Generate traffic to a single URL."""
    for _ in range(num_requests):
        send_request(url, proxy)
        time.sleep(random.uniform(0.5, 2))

def start_traffic(urls, min_requests, max_requests, proxy):
    """Start generating traffic for all URLs using a ThreadPoolExecutor."""
    with ThreadPoolExecutor() as executor:
        for url in urls:
            num_requests = random.randint(min_requests, max_requests)
            executor.submit(generate_traffic, url, num_requests, proxy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate HTTP traffic to specified URLs.')
    parser.add_argument('--file', type=str, required=True, help='Text file containing URLs (one per line)')
    parser.add_argument('--min_requests', type=int, default=50, help='Minimum number of requests per URL')
    parser.add_argument('--max_requests', type=int, default=100, help='Maximum number of requests per URL')
    parser.add_argument('--proxy', type=str, help='Proxy server URL (e.g., http://username:password@proxyserver:port)')

    args = parser.parse_args()

    urls = load_urls_from_file(args.file)
    proxy = {"http": args.proxy, "https": args.proxy} if args.proxy else None

    logging.info("Starting traffic generation...")
    start_traffic(urls, args.min_requests, args.max_requests, proxy)
    logging.info("Traffic generation completed.")

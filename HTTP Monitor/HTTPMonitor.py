"""
Simple HTTP monitor

Reads 'targets.txt' (list of URLs), checks their HTTP status,
and writes results to 'monitor.log' with timestamps.
"""
import requests
import logging

# Create logging config (how logs will look)
logging.basicConfig(
    filename='monitor.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Opens targets.txt file and reads it
with open('targets.txt', 'r') as t:
    targets = [line.strip() for line in t.readlines()]

    print(targets)

# Gets request for every site in targets.txt and checks their status code
for target in targets:
    r = requests.get(target, timeout=5)
    status = r.status_code
    if status == 200:
        logging.info(f'{target} is working')
    else:
        logging.warning(f'{target} returned status {status}')



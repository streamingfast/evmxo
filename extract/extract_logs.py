import json
import requests
import threading
import re

def unpack_payload(text_payload):
    match = re.search("{.*}", text_payload).group()
    resp = json.loads(match)
    return resp['request']

def process_payload(logs, thread_id, idx_start, idx_end):
    for idx, log in enumerate(logs[idx_start:idx_end]):
        payload = unpack_payload(log['textPayload'])

        print('processing request {} in thread {}'.format(idx, thread_id))
        # logger.info('processing request {} in thread {}'.format(idx, thread_id))
        resp = requests.post(url, data=payload, headers=headers)

logs_suffix = '20230314'
with open('data/downloaded-logs-{}.json'.format(logs_suffix)) as f:
    logs = json.load(f)

url = 'http://localhost:8080'
headers = {'Content-Type': 'application/json'}
threads = 16

jobs = []
logs_length = len(logs)
batch_size = int(logs_length / threads)

for i in range(0, threads):
    thread = threading.Thread(target=process_payload, args=(logs, i, batch_size * i, batch_size * (i + 1)))
    jobs.append(thread)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

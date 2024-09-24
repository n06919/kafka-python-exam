from kafka import KafkaProducer
import re
import csv
import json
import time
from datetime import datetime

# test

brokers = ['localhost:29092', 'localhost:39092', 'localhost:49092']
producer = KafkaProducer(
    bootstrap_servers=brokers,
    acks=-1
)

topicName = 'skcc-college'

for _ in range(1):
    with open("./u.data", "rb") as file:
        for i in file:
            row = i.decode()
            data = re.split('\t|\n', row)[:5]
            data[4] = datetime.fromtimestamp(int(data[4]))\
                .strftime('%Y-%m-%d %H:%M:%S')
            producer.send(topicName, json.dumps(data).encode('utf-8'))
            print(data)
            time.sleep(0.15)
#from typing import Any, Union

#import a as a
from kafka import KafkaProducer
# from time import sleep, time
import time

# import consumer_kafka

i = 1
count = 1
producer = KafkaProducer(bootstrap_servers='test:9092')
topic = "rep-topic2"

while i:
    message = f'test message {count}'
    future = producer.send(topic, bytes(message, encoding='utf-8'))
    record_metadata = future.get(timeout=60)
    print("topic name =", record_metadata.topic, "  partition name =", record_metadata.partition, "  offset =",
          record_metadata.offset, "  message =", message)
        # print(record_metadata)
    time.sleep(1)
    count += 1



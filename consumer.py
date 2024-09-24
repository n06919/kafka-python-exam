from kafka import KafkaConsumer
import json

brokers = ['localhost:29092', 'localhost:39092', 'localhost:49092']
topicName = 'skcc-college'
consumer = KafkaConsumer(
    topicName,
    bootstrap_servers=brokers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id="my-group",
)

for message in consumer:
    print("Topic: {}, Partition: {}, Offset: {}, Key: {}, Value: {}".format(
        message.topic,
        message.partition,
        message.offset,
        message.key,
        message.value.decode('utf-8'))
    )

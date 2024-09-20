# kafka-python-exam
```
python3 -m venv venv
source venv/bin/activate

pip install kafka-python
```

### Consumer Run ###
```
python3 kafka_consumer.py
Waiting for messages...
Received message: {'message': 'Hello, Kafka!'}

```

### Producer Run ###
```
python3 kafka_producer.py

Enter message to send to Kafka (type 'exit' to quit): hello-kafka
Sent message: {'message': 'hello-kafka'}
Enter message to send to Kafka (type 'exit' to quit):

```

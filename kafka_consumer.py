from kafka import KafkaConsumer
import json

class KafkaConsumerClient:
    def __init__(self, server='localhost:9092'):
        self.consumer = KafkaConsumer(
            'test_topic',
            bootstrap_servers=[server],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='test-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # JSON 역직렬화
        )

    def consume_messages(self):
        print("Waiting for messages...")
        for message in self.consumer:
            print(f"Received message: {message.value}")

# 컨슈머 인스턴스 생성 및 메시지 소비
if __name__ == '__main__':
    consumer = KafkaConsumerClient()
    consumer.consume_messages()

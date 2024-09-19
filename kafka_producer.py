from kafka import KafkaProducer
import json

class KafkaProducerClient:
    def __init__(self, server='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=[server],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON 직렬화
        )
        self.topic = 'test_topic'

    def send_message(self, message):
        future = self.producer.send(self.topic, message)
        result = future.get(timeout=60)  # 전송 결과 기다림
        print(f"Sent message: {message}")
        return result

# 사용자 입력을 받아 메시지를 Kafka로 전송
if __name__ == '__main__':
    producer = KafkaProducerClient()

    while True:
        message = input("Enter message to send to Kafka (type 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Exiting...")
            break
        producer.send_message({'message': message})

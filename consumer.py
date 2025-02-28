from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'student-results',
    bootstrap_servers='localhost:9093',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    print("Received Result:", message.value)


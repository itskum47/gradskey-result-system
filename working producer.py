from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

test_data = [
    {"student_id": 101, "subject": "Math", "marks": 95, "grade": "A"},
    {"student_id": 102, "subject": "Science", "marks": 88, "grade": "B"}
]

for record in test_data:
    producer.send("test-topic", record)
    print(f"Sent: {record}")
    time.sleep(1)

producer.flush()


from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

result_data = {
    "student_id": 101,
    "subject": "Mathematics",
    "marks": 95,
    "grade": "A"
}

producer.send('student-results', result_data)
print("Sent:", result_data)


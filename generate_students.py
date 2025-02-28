import pandas as pd
import random

students = []
for i in range(1, 10001):  # 10,000 students
    students.append({
        "roll_no": f"GRADSKEY{i:05}",
        "name": f"Student_{i}",
        "math": random.randint(30, 100),
        "physics": random.randint(30, 100),
        "chemistry": random.randint(30, 100),
        "english": random.randint(30, 100),
        "cs": random.randint(30, 100),
        "economics": random.randint(30, 100)
    })

df = pd.DataFrame(students)
df.to_csv("students.csv", index=False)
print("Generated students.csv")


# GradsKey Result Management System 📊

A scalable result management system using **Apache Spark, Kafka, Hadoop, and PostgreSQL**, designed for efficient student result processing and real-time data streaming.

---

## 🚀 Features
- 🔥 **Batch & Streaming Processing** with **Apache Spark**
- 📡 **Kafka Integration** for real-time data streaming
- 🏪 **PostgreSQL Database** for persistent storage
- 📊 **Visual Dashboard** to view results
- 🐳 **Dockerized Setup** for easy deployment
- ⚡ **Cross-platform compatibility** (Windows, Mac, Linux)

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Piyush12223821/gradskey-result-system.git
cd gradskey-result-system
```

### **2️⃣ Install Dependencies**
Make sure you have **Docker & Docker Compose** installed.

For manual installation:
```bash
pip install -r requirements.txt
```

---

## 🐳 Run with Docker (Recommended)
```bash
docker-compose up --build
```
This will start **PostgreSQL, Kafka, Spark, and the web dashboard**.

---

## 🏗️ Manual Setup (Without Docker)

### **1️⃣ Start PostgreSQL**
```bash
docker run --name postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -e POSTGRES_DB=gradskey -p 5432:5432 -d postgres
```

### **2️⃣ Apply Database Schema**
```bash
psql -U admin -d gradskey -f sql/init.sql
```

### **3️⃣ Start Kafka**
Make sure **Zookeeper** and **Kafka** are running:
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

### **4️⃣ Run Spark Streaming**
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_streaming.py
```

---

## 📡 Producing and Consuming Messages

### **Send Student Data to Kafka**
```bash
python producer.py
```

### **Consume Data from Kafka**
```bash
python consumer.py
```

---

## 📊 Access the Dashboard
Once everything is running, open:
```
http://localhost:3000
```
View **student results** and **feedback analysis**.

---

## 🛠️ Development

### **Run Tests**
```bash
pytest
```

### **Format Code**
```bash
black .
```

---

## 📜 License
This project is **MIT Licensed**. Feel free to use and contribute! 🚀


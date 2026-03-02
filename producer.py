import psycopg2
from kafka import KafkaProducer
from config import *
import json
import time

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

conn = psycopg2.connect(
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
    )

cursor = conn.cursor()


cursor.execute("SELECT id, username, event_type, extract(epoch FROM event_time) FROM user_logins WHERE sent_to_kafka=FALSE")
rows = cursor.fetchall()

for row in rows:
    data = {
        "id": row[0],
        "user": row[1],
        "event": row[2],
        "timestamp": float(row[3])  # преобразуем Decimal → float
    }
    producer.send("user_events", value=data)
    cursor.execute("UPDATE user_logins SET sent_to_kafka=TRUE WHERE id = %s", (row[0],))
    conn.commit()
    print("Sent:", data)
    time.sleep(0.5)
import psycopg2
import clickhouse_connect
import os
from dotenv import load_dotenv

load_dotenv()


#Postgre конфигурация
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")



#ClickHouse конфигурация
CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST')
CLICKHOUSE_PORT = os.getenv('CLICKHOUSE_PORT')
CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER')
CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD')



#Kafka конфигурация
BOOTSTRAP_SERVERS = os.getenv('KAFKA_HOST')
TOPIC = os.getenv('KAFKA_TOPIC')
GROUP_ID=os.getenv('KAFKA_GROUP_ID')
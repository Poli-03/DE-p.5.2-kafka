# DE-p.5.2-kafka

1. запускаем docker-compose.yml
2. в Postgre добавляем ALTER TABLE user_logins ADD COLUMN sent_to_kafka BOOLEAN DEFAULT FALSE;
3. SELECT * FROM your_table_name 
   WHERE sent_to_kafka = FALSE;
4. UPDATE user_logins 
   SET sent_to_kafka = TRUE
   WHERE sent_to_kafka = FALSE;
5. заупскаем python producer.py
6. заупскаем python consumer.py
7. проверяем в clickhouse через select count(distinct *) from user_logins ul

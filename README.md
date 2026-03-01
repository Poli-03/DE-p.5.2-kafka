# DE-p.5.2-kafka

1. запускаем docker-compose.yml
2. в sql скрипте сгенерированная таблица
3. в Postgre добавляем ALTER TABLE user_logins ADD COLUMN sent_to_kafka BOOLEAN DEFAULT FALSE;
4. заупскаем python producer.py   
5. заупскаем python consumer.py
6. UPDATE user_logins 
   SET sent_to_kafka = TRUE
   WHERE id IN (
       SELECT id FROM user_logins
       WHERE sent_to_kafka = FALSE
       LIMIT 1000);
7. проверяем в clickhouse через select count(distinct *) from user_logins ul

# DE-p.5.2-kafka

1. запускаем docker-compose.yml
2. в Postgre добавляем ALTER TABLE user_logins ADD COLUMN sent_to_kafka BOOLEAN DEFAULT FALSE;
3. заупскаем python producer.py
4. заупскаем python consumer.py
5. проверяем в clickhouse через select count(distinct *) from user_logins ul

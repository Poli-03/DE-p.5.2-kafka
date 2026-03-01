# DE-p.5.2-kafka

1. запускаем docker-compose.yml
2. заупскаем python producer.py #из=за того, то БД создается рандомом в продюсере, то сначала запускаем его,
   если бы БД была изначало в Postgre, то можно было бы запустить его 4м пунктом
3.  в Postgre добавляем ALTER TABLE user_logins ADD COLUMN sent_to_kafka BOOLEAN DEFAULT FALSE;
4. SELECT * FROM user_logins 
   WHERE sent_to_kafka = FALSE
   LIMIT 1000;
5. заупскаем python consumer.py
6. UPDATE user_logins 
   SET sent_to_kafka = TRUE
   WHERE id IN (
       SELECT id FROM user_logins
       WHERE sent_to_kafka = FALSE
       LIMIT 1000);
7. проверяем в clickhouse через select count(distinct *) from user_logins ul

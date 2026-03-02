create table user_logins(
    id SERIAL primary key,
    username text not null,
    event_type text not null,
    event_time timestamp not null,
    sent_to_kafka boolean default false
);

insert into user_logins (username, event_type, event_time)
select
    case (random()*3)::int
        when 0 then 'micha'
        when 1 then 'alica'
        when 2 then 'bob'
        else 'nina'
    end as username,

    'login' as event_type,

    now() - (random() * interval '1 minute') as event_time
from generate_series(1, 100) as generated_id;
# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
    SONGPLAY_ID   SERIAL PRIMARY KEY,
    START_TIME    TIMESTAMP NOT NULL,
    USER_ID       INT NOT NULL,
    LEVEL         VARCHAR,
    SONG_ID       VARCHAR,
    ARTIST_ID     VARCHAR,
    SESSION_ID    INT,
    LOCATION      VARCHAR,
    USER_AGENT    VARCHAR
) """)

user_table_create = (""" CREATE TABLE IF NOT EXISTS USERS (
    USER_ID      VARCHAR PRIMARY KEY,
    FIRST_NAME   VARCHAR,
    LAST_NAME    VARCHAR,
    GENDER       VARCHAR,
    LEVEL        VARCHAR
)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS SONGS (
    SONG_ID     VARCHAR  PRIMARY KEY,
    title       VARCHAR,
    ARTIST_ID   VARCHAR,
    YEAR        INT,
    DURATION    NUMERIC (10, 2)
) 
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
    ARTIST_ID   VARCHAR PRIMARY KEY,
    NAME        VARCHAR,
    LOCATION    VARCHAR,
    LATTITUDE   NUMERIC (10, 2),
    LONGITUDE   NUMERIC (10, 2)
) 
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS TIME (
    START_TIME   TIMESTAMP PRIMARY KEY,
    HOUR         INT,
    DAY          VARCHAR,
    WEEK         VARCHAR,
    MONTH        VARCHAR,
    YEAR         INT,
    WEEKDAY      VARCHAR
)
""")

# INSERT RECORDS

songplay_table_insert = (""" insert into songplays( songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = (""" insert into users( user_id, first_name, last_name, gender, level)
values(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = (""" insert into songs( song_id, title, artist_id, year, duration)
values(%s,%s,%s,%s,%s)
ON CONFLICT (song_id) 
DO NOTHING;
""")

artist_table_insert = (""" insert into artists( artist_id, name, location, lattitude, longitude)
values(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) 
DO NOTHING;
""")


time_table_insert = (""" insert into time( start_time, hour, day, week, month, year, weekday)
values(%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT (start_time) 
DO NOTHING;
""")

# FIND SONGS

song_select = ("""  SELECT s.song_id, a.artist_id
   FROM songs s
   JOIN artists a
   ON s.artist_id = a.artist_id
   WHERE s.title=(%s) AND a.name=(%s) AND s.duration=(%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
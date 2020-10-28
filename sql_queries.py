# DROP TABLES
songplays_table_drop = 'DROP TABLE IF EXISTS songplays'
users_table_drop = 'DROP TABLE IF EXISTS users'
songs_table_drop = 'DROP TABLE IF EXISTS songs'
artists_table_drop = 'DROP TABLE IF EXISTS artists'
time_table_drop = 'DROP TABLE IF EXISTS time'


# CREATE TABLES
users_table_create = ('''CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
                                                        first_name varchar,
                                                        last_name varchar,
                                                        gender varchar,
                                                        level varchar)''')


songs_table_create = ('''CREATE TABLE IF NOT EXISTS songs (song_id int PRIMARY KEY,
                                                        title varchar,
                                                        artist_id int,
                                                        year int,
                                                        duration NUMERIC(10,5))''')

artist_table_create = ('''CREATE TABLE IF NOT EXISTS artists (artist_id int PRIMARY KEY,
                                                        name varchar,
                                                        location varchar,
                                                        latitude decimal,
                                                        longitude decimal)''')

time_table_create = ('''CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP NOT NULL PRIMARY KEY,
                                                        hour int,
                                                        day int,
                                                        week int,
                                                        month int,
                                                        year int,
                                                        weekday varchar)''')

songplays_table_create = ('''CREATE TABLE IF NOT EXISTS songplays(songplay_id bigserial PRIMARY KEY,
                                                        start_time TIMESTAMP NOT NULL,
                                                        user_id int NOT NULL REFERENCES users(user_id),
                                                        level varchar,
                                                        song_id int REFERENCES songs(song_id),
                                                        artist_id int REFERENCES artists(artist_id),
                                                        session_id int,
                                                        location varchar,
                                                        user_agent varchar)''')


# QUERY LIST
create_table_queries = [users_table_create, songs_table_create, artist_table_create, time_table_create, songs_table_create]

drop_table_queries = [users_table_drop, songs_table_drop, artists_table_drop, time_table_drop, songplays_table_drop]
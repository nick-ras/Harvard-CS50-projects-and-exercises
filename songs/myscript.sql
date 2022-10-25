
select name from songs asc;
select name from songs order by name asc;
select name from songs order by duration_ms asc LIMIT 5;
select name from songs where danceability AND energy AND valence > 0.75;
sqlite> select avg(energy) from songs;
sqlite> select name from songs where id IN (select id from artists where name = 'Post Malone');
select avg(energy) from songs where id IN (select id from artists where name = 'Drake');
select name from songs where name LIKE '%(%';


-- CREATE TABLE songs (
--     id INTEGER,
--     name TEXT,
--     artist_id INTEGER,
--     danceability REAL,
--     energy REAL,
--     key INTEGER,
--     loudness REAL,
--     speechiness REAL,
--     valence REAL,
--     tempo REAL,
--     duration_ms INTEGER
-- );
-- CREATE TABLE artists (
--     id INTEGER,
--     name TEXT
-- );
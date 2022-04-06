CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)



CREATE TABLE IF NOT EXISTS data_types_demos(
	user_age TINYINT(8) UNSIGNED,
	salary DECIMAL(6,2) NOT NULL UNIQUE ,
	user_name  varchar(10),
	avatar blob,
	created_at datetime,
	updated_at timestamp
);



-- '1953-09-02', 'Georgi', 'Facello', 'M', '1986-06-26', 100000, '2019-01-01 00:00:00',
-- '1953-09-02', 'Georgi', 'Facello', 'M', '1986-06-26', 100300, '2017-01-01 00:00:00',

-- INSERT INTO table_name [(column, ...)]
-- VALUES (value, ...)[, (...), ...];

INSERT INTO artist VALUES (10, 'Ivan', 'Ivanov', 100);

INSERT INTO artist (lname, fname)
VALUES ('Petrov	','Petr'),
('Sidorov','Sidor');


DELETE FROM artist
WHERE lname='Ivanov;

ALTER TABLE test.artist ADD INDEX(fname(10));

INSERT INTO artist (lname) VALUES ('Ivanov');



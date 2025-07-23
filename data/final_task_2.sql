DROP TABLE IF EXISTS firstname
;

CREATE TABLE firstname (
    id serial PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL)
;

DROP TABLE IF EXISTS surname
;

CREATE TABLE surname (
    id serial PRIMARY KEY,
    surname VARCHAR(30) NOT NULL)
;

DROP TABLE IF EXISTS lastname
;

CREATE TABLE lastname (
    id serial PRIMARY KEY,
    lastname VARCHAR(30) NOT NULL)
;

INSERT INTO firstname (firstname)
 VALUES ('Иванов'),
		('Петров'),
		('Сидоров')
;

INSERT INTO surname (surname)
 VALUES ('Иван'),
		('Петр'),
		('Сидор')
;

INSERT INTO lastname (lastname)
 VALUES ('Иванович'),
		('Петрович'),
		('Сидорович')
;

SELECT CONCAT(f.firstname, " ", s.surname, " ", l.lastname) AS full_name
FROM firstname AS f
JOIN surname AS s ON f.id = s.id
JOIN lastname AS l ON f.id = l.id
ORDER BY 1 DESC
;
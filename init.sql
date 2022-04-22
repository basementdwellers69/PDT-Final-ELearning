-- mysql table, if not exist please download xampp

CREATE DATABASE IF NOT EXISTS `pdt` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `pdt`;




-- DROP TABLE IF EXISTS major;
-- CREATE TABLE major (
--     id SERIAL PRIMARY KEY,
--     major_name VARCHAR (255) NOT NULL
-- );

-- DROP TABLE IF EXISTS users;
-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     status INT NOT NULL,
--     firstName VARCHAR(255) NOT NULL,
--     lastName VARCHAR (255),
--     username VARCHAR(100) UNIQUE NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     password VARCHAR(255) NOT NULL,
--     major_id INT,
--     CONSTRAINT fk_major FOREIGN KEY (major_id) REFERENCES major(id)
-- );

-- DROP TABLE IF EXISTS articles;
-- CREATE TABLE articles (
--     id SERIAL PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     body TEXT NOT NULL,
--     user_id INT,
--     CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
-- );

-- INSERT INTO major (major_name) VALUES ('Information Technology'), ('Information System'), ('Visual Communication Design');

-- INSERT INTO users (id, status, firstName, lastName, username, email, password, major_id)
-- VALUES ('');

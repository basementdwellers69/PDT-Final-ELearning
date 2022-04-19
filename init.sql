DROP TABLE IF EXISTS major;
CREATE TABLE major (
    id SERIAL PRIMARY KEY,
    major_name VARCHAR (255) NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    status CHAR(20) NOT NULL UNIQUE KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR (255),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    major_id INT,
    status VARCHAR(255) NOT NULL,
    CONSTRAINT fk_major FOREIGN KEY (major_id) REFERENCES major(id)
);

DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (id, status, firstName, lastName, username, email, password, major_id)
VALUES ('');

INSERT INTO major (major_name) VALUES ('Information Technology'), ('Information System'), ('Visual Communication Design');

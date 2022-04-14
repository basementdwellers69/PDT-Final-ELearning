DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR (255),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    major_id INT,
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

DROP TABLE IF EXISTS major;
CREATE TABLE major (
    id SERIAL PRIMARY KEY,
    major_name VARCHAR (255) NOT NULL
);

INSERT INTO users (username, name, password) VALUES ('admin', 'Administrator', 'admin');

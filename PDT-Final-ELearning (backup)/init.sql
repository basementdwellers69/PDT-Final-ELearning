DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(250) NOT NULL,
    lastname VARCHAR(250) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    address VARCHAR(300),
    city VARCHAR(100),
    country VARCHAR(255),
    postalcode INT,
    majorId INT,
    CONSTRAINT fk_major FOREIGN KEY (majorId) REFERENCES major(id),
    statusId INT,
    CONSTRAINT fk_status FOREIGN KEY (statusId) REFERENCES status(id),
);

DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS status;
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
);

DROP TABLE IF EXISTS major;
CREATE TABLE major (
    id SERIAL PRIMARY KEY,
    major_name VARCHAR(255) NOT NULL,
    
);

DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    room VARCHAR(255),
    classlink TEXT,
    lecturerId INT,
    CONSTRAINT fk_lecturer FOREIGN KEY (lecturerId) REFERENCES users(id)
);

DROP TABLE IF EXISTS course_content;
CREATE TABLE course_content (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    link TEXT NOT NULL,
    courseId INT,
    CONSTRAINT fk_courses FOREIGN KEY (courseId) REFERENCES courses(id)
);

INSERT INTO users (firstname, lastname, username, email, password, address, city, country, postalcode, statusId, majorId, courseId) VALUES ('Admin', 'Administrator', 'admin', 'admin@ecampus.com', 'Admin', '221B Baker Street', 'Bekasi', 'Indonesia', 12343, 1, 1, 1);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO posts (title, content) 
VALUES ('Test Post', 'This is a test content.');


SELECT * FROM posts;
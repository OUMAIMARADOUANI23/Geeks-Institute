import db from '../config/db.js';

export const getAllPosts = () => {
    return db.query('SELECT * FROM posts ORDER BY id ASC');
};

export const getPostById = (id) => {
    return db.query('SELECT * FROM posts WHERE id = $1', [id]);
};

export const createPost = (title, content) => {
    return db.query(
        'INSERT INTO posts (title, content) VALUES ($1, $2) RETURNING *',
        [title, content]
    );
};

export const updatePost = (id, title, content) => {
    return db.query(
        'UPDATE posts SET title=$1, content=$2 WHERE id=$3 RETURNING *',
        [title, content, id]
    );
};

export const deletePost = (id) => {
    return db.query('DELETE FROM posts WHERE id=$1 RETURNING *', [id]);
};

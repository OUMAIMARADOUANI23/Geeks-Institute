import * as Post from '../models/postModel.js';

export const getPosts = async (req, res) => {
    try {
        const result = await Post.getAllPosts();
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

export const getPost = async (req, res) => {
    try {
        const result = await Post.getPostById(req.params.id);
        if (result.rows.length === 0) return res.status(404).json({ message: 'Post not found' });
        res.json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

export const createNewPost = async (req, res) => {
    try {
        const { title, content } = req.body;
        const result = await Post.createPost(title, content);
        res.status(201).json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

export const updateExistingPost = async (req, res) => {
    try {
        const { title, content } = req.body;
        const result = await Post.updatePost(req.params.id, title, content);
        if (result.rows.length === 0) return res.status(404).json({ message: 'Post not found' });
        res.json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

export const deleteExistingPost = async (req, res) => {
    try {
        const result = await Post.deletePost(req.params.id);
        if (result.rows.length === 0) return res.status(404).json({ message: 'Post not found' });
        res.json({ message: 'Post deleted', post: result.rows[0] });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

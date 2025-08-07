const express = require('express');
const app = express();
const port = 3000;
app.use(express.json());

let posts = [
  { id: 1, title: 'First Post', content: 'This is my first blog post' },
  { id: 2, title: 'Second Post', content: 'This is another post' }
];

app.get('/posts', (req, res) => {
  res.json(posts);
});

app.get('/posts/:id', (req, res) => {
  const post = posts.find(p => p.id === parseInt(req.params.id));
  if (!post) return res.status(404).send('Post not found');
  res.json(post);
});

app.post('/posts', (req, res) => {
  const newPost = {
    id: posts.length + 1,
    title: req.body.title,
    content: req.body.content
  };
  posts.push(newPost);
  res.status(201).json(newPost);
});

app.put('/posts/:id', (req, res) => {
  const post = posts.find(p => p.id === parseInt(req.params.id));
  if (!post) return res.status(404).send('Post not found');
  post.title = req.body.title;
  post.content = req.body.content;
  res.json(post);
});

app.delete('/posts/:id', (req, res) => {
  const index = posts.findIndex(p => p.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).send('Post not found');
  const deletedPost = posts.splice(index, 1);
  res.json(deletedPost[0]);
});

app.use((req, res) => {
  res.status(404).send('Route not found');
});

app.listen(port, () => {
  console.log(`Blog API is running at http://localhost:${port}`);
});
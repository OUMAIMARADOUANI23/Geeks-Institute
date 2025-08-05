const express = require('express');
const { fetchPosts } = require('./data/dataService');
const app = express();
const PORT = 5000;

app.use(express.json());

app.get('/api/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();
    console.log("Données récupérées avec succès et envoyées !");
    res.json(posts);
  } catch (error) {
    res.status(500).json({ message: 'Erreur lors de la récupération des posts' });
  }
});


app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

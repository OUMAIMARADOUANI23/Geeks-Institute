const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

const todoRoutes = require('./routes/todos');
app.use('/todos', todoRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

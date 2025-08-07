const express = require('express');
const session = require('express-session');
const quizRouter = require('./routes/quiz');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(session({
  secret: 'trivia-secret',
  resave: false,
  saveUninitialized: true
}));

app.use('/quiz', quizRouter);

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

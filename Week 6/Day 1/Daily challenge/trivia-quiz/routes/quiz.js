const express = require('express');
const router = express.Router();

const triviaQuestions = [
  { question: "What is the capital of France?", answer: "Paris" },
  { question: "Which planet is known as the Red Planet?", answer: "Mars" },
  { question: "What is the largest mammal in the world?", answer: "Blue whale" }
];

router.get('/', (req, res) => {
  req.session.currentQuestion = 0;
  req.session.score = 0;

  const question = triviaQuestions[0].question;
  res.send(`Question 1: ${question}`);
});

router.post('/', (req, res) => {
  const userAnswer = req.body.answer;
  const currentIndex = req.session.currentQuestion;

  if (currentIndex >= triviaQuestions.length) {
    return res.redirect('/quiz/score');
  }

  const correctAnswer = triviaQuestions[currentIndex].answer;

  if (userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()) {
    req.session.score += 1;
    feedback = "✅ Correct!";
  } else {
    feedback = `❌ Incorrect. The correct answer was: ${correctAnswer}`;
  }

  req.session.currentQuestion += 1;

  if (req.session.currentQuestion < triviaQuestions.length) {
    const nextQuestion = triviaQuestions[req.session.currentQuestion].question;
    res.send(`${feedback}<br><br>Next Question: ${nextQuestion}`);
  } else {
    res.redirect('/quiz/score');
  }
});

router.get('/score', (req, res) => {
  const score = req.session.score || 0;
  const total = triviaQuestions.length;
  res.send(`🎉 Quiz Finished! Your final score is: ${score}/${total}`);
});

module.exports = router;

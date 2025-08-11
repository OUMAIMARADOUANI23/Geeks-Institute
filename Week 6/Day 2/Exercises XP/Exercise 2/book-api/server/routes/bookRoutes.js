const express = require('express');
const router = express.Router();

const bookController = require('../controllers/bookController');

router.get('/books', bookController.getBooks);
router.get('/books/:bookId', bookController.getBook);
router.post('/books', bookController.createBook);

module.exports = router;

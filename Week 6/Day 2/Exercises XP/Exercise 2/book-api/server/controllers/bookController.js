const Book = require('../models/bookModel');

const getBooks = (req, res) => {
  const books = Book.getAllBooks();
  res.json(books);
};

const getBook = (req, res) => {
  const bookId = parseInt(req.params.bookId);
  const book = Book.getBookById(bookId);
  if (!book) {
    return res.status(404).json({ message: 'Book not found' });
  }
  res.json(book);
};

const createBook = (req, res) => {
  const { title, author, publishedYear } = req.body;
  if (!title || !author || !publishedYear) {
    return res.status(400).json({ message: 'Please provide title, author and publishedYear' });
  }
  const books = Book.getAllBooks();
  const newBook = {
    id: books.length > 0 ? books[books.length - 1].id + 1 : 1,
    title,
    author,
    publishedYear,
  };
  Book.createBook(newBook);
  res.status(201).json(newBook);
};

module.exports = {
  getBooks,
  getBook,
  createBook,
};

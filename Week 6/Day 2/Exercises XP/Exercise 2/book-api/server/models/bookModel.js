const books = require('../config/db');

const getAllBooks = () => books;

const getBookById = (id) => books.find(book => book.id === id);

const createBook = (newBook) => {
  books.push(newBook);
  return newBook;
};

module.exports = {
  getAllBooks,
  getBookById,
  createBook,
};

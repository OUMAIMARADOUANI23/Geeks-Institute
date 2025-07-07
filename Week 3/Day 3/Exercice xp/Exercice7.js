const allBooks = [
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://m.media-amazon.com/images/I/81t2CVWEsUL._AC_UF1000,1000_QL80_.jpg",
    alreadyRead: true
  },
  {
    title: "1984",
    author: "George Orwell",
    image: "https://m.media-amazon.com/images/I/71kxa1-0mfL._AC_UF1000,1000_QL80_.jpg",
    alreadyRead: false
  }
];

const section = document.querySelector(".listBooks");

allBooks.forEach(book => {
  const bookDiv = document.createElement("div");
  bookDiv.classList.add("book");

  if (book.alreadyRead) {
    bookDiv.classList.add("read");
  }

  const text = document.createElement("p");
  text.textContent = `${book.title} written by ${book.author}`;

  const image = document.createElement("img");
  image.src = book.image;

  bookDiv.appendChild(text);
  bookDiv.appendChild(image);

  section.appendChild(bookDiv);
});

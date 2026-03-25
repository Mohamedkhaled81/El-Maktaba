import BookModel from "../models/book.model.js";

const renderAllBooks = async function (req, res) {
    res.render('allBooks');
};
const renderAddBook = function (req, res) {
    res.render('addBook');
};


//! Handle This Controller in more cleaner way
const addBook = async function (req, res) {
    console.log(req.body);
    let {title, publishedYear, authors, categories, description} = req.body;
    if(!title || ! publishedYear || !authors || !categories || !description) {
        //! GLOBAL ERROR Handling is required
        throw new Error('Bad request');
    }
    publishedYear = Number(publishedYear);
    if(Number.isNaN(publishedYear)) {
        throw new Error('Bad request');
    }
    authors = authors.split(',').map((authorName) => authorName.trim());
    categories = categories.split(',').map((categoryName) => categoryName.trim());

    const book = new BookModel({title, publishedYear, authors, categories, description});
    try {
        await book.save();
    }catch(err) {
        res.send('ERROR');
    }
    res.redirect('/books/allBooks');
};

const updateBook = async function (req, res) {};
const deleteBook = async function (req, res) {};


export {renderAddBook, renderAllBooks, addBook, updateBook, deleteBook};
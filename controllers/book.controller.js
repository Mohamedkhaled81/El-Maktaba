import BookModel from "../models/book.model.js";
import commaToArray from "../utils/commaToArray.js";

//* CRUD ON BOOK RESOURCE
const addBook = async function (req, res) {
    let {title, publishedYear, authors, categories, description} = req.body;
    
    publishedYear = Number(publishedYear);
    authors = commaToArray(authors);
    categories = commaToArray(categories);
    
    const book = new BookModel({title, publishedYear, authors, categories, description});
    await book.save();

    res.redirect('/books/allBooks');
};

const updateBook = async function (req, res) {
    const id = req.params.id;
    const payLoad = req.body;

    payLoad.authors = commaToArray(payLoad.authors);
    payLoad.categories = commaToArray(payLoad.categories);

    await BookModel.findByIdAndUpdate(id, payLoad);

    res.redirect('/books/allBooks');
};

const deleteBook = async function (req, res) {
    const _id = req.params.id;

    await BookModel.deleteOne({_id});

    res.redirect('/books/allBooks');
};

//* Handling RENDERING FUNCTIONS
const renderAllBooks = async function (req, res) {
    const books = await BookModel.find();

    res.render('allBooks', {books});
};

const renderAddBook = function (req, res) {
    res.render('addBook');
};

const renderEditBook = async function (req, res) {
    const id = req.params.id;

    const book = await BookModel.findById(id);

    res.render('editBook', {book});
}

export {renderEditBook, renderAddBook, renderAllBooks, addBook, updateBook, deleteBook};
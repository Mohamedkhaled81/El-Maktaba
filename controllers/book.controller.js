import BookModel from "../models/book.model.js";

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

//! Handle This Controller in more cleaner way
const addBook = async function (req, res) {
    try{
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
        await book.save();
    }
    catch(err) {
        res.send('ERROR');
    }
    res.redirect('/books/allBooks');
};

const updateBook = async function (req, res) {
    const id = req.params.id;
    const payLoad = req.body;

    payLoad.authors = payLoad.authors.split(',').map((author) => author.trim());
    payLoad.categories = payLoad.categories.split(',').map((category) => category.trim());

    console.log(payLoad);

    await BookModel.findByIdAndUpdate(id, payLoad);
    res.redirect('/books/allBooks');
};
const deleteBook = async function (req, res) {
    const _id = req.params.id;
    await BookModel.deleteOne({_id});
    res.redirect('/books/allBooks');
};


export {renderEditBook, renderAddBook, renderAllBooks, addBook, updateBook, deleteBook};
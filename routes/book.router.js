import { Router } from "express";
import {renderAddBook, addBook, renderAllBooks, renderEditBook,deleteBook} from '../controllers/book.controller.js';

const bookRouter = Router();

bookRouter.get('/allBooks', renderAllBooks);
bookRouter.get('/addBook', renderAddBook);
bookRouter.get('/EditBook/:id', renderEditBook);

bookRouter.post('/', addBook);
bookRouter.put('/:id', (req, res) => {});
bookRouter.delete('/:id', deleteBook);

export default bookRouter;
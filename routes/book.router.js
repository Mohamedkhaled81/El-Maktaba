import { Router } from "express";
import {renderAddBook, renderAllBooks, renderEditBook, addBook, deleteBook, updateBook} from '../controllers/book.controller.js';

const bookRouter = Router();

bookRouter.get('/allBooks', renderAllBooks);
bookRouter.get('/addBook', renderAddBook);
bookRouter.get('/EditBook/:id', renderEditBook);

bookRouter.post('/', addBook);
bookRouter.put('/:id', updateBook);
bookRouter.delete('/:id', deleteBook);

export default bookRouter;
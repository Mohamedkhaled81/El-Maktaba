import { Router } from "express";
import {renderAddBook, renderAllBooks, renderEditBook, addBook, deleteBook, updateBook} from '../controllers/book.controller.js';
import validateRequest from "../middlewares/validateRequest.js";
import { BookValidator } from "../validators/book.validator..js";

const bookRouter = Router();

bookRouter.get('/allBooks', renderAllBooks);
bookRouter.get('/addBook', renderAddBook);
bookRouter.get('/EditBook/:id', renderEditBook);

bookRouter.post('/', BookValidator, validateRequest, addBook);
bookRouter.put('/:id', BookValidator, validateRequest, updateBook);
bookRouter.delete('/:id', deleteBook);

export default bookRouter;
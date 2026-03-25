import { Router } from "express";
import {renderAddBook, addBook, renderAllBooks} from '../controllers/book.controller.js';

const bookRouter = Router();

bookRouter.get('/allBooks', renderAllBooks);
bookRouter.get('/addBook', renderAddBook);
bookRouter.get('/EditBook', (req, res) => {});

bookRouter.post('/', addBook);
bookRouter.put('/:id', (req, res) => {});
bookRouter.delete('/:id', (req, res) => {});

export default bookRouter;
import { Router } from "express";
import bookRouter from "./book.router.js";

const rootRouter = Router();

rootRouter.get('/', (req, res) => {
    res.render('main');
});

rootRouter.use('/books', bookRouter);
rootRouter.use((req, res) => {res.status(404).send(`<h1>Not-Found</h1>`)});

export default rootRouter;
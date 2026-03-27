import { Router } from "express";
import bookRouter from "./book.router.js";
import CustomError from "../utils/customError.js";

const rootRouter = Router();

rootRouter.get('/home', (req, res) => {
    res.render('main');
});

rootRouter.use('/books', bookRouter);
rootRouter.use((req, res, next) => {
    const err = new CustomError("Can't find a route on the server!", 404);
    next(err);
});

export default rootRouter;
import { validationResult } from "express-validator"
import CustomError from "../utils/customError.js";

const validateRequest = function (req, res, next) {
    const errors = validationResult(req);
    if(!errors.isEmpty()) {
        const BadReqErr = new CustomError(errors.array()[0]["msg"], 400);
        next(BadReqErr);
    }
    next();
}

export default validateRequest;
export default class CustomError extends Error {
    constructor(mssg, statusCode) {
        super(mssg);
        this.statusCode = statusCode;

        Error.captureStackTrace(this, this.constructor);
    }
}
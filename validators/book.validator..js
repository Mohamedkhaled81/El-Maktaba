import { body } from "express-validator";

export const BookValidator = [
    body('title')
        .notEmpty().withMessage('Title is required')
        .isString().withMessage('Title must be a string'),

    body('description')
        .notEmpty().withMessage('Description is required'),

    body('publishedYear')
        .notEmpty().withMessage('Published year is required')
        .isInt({ min: 0, max: (new Date().getUTCFullYear()) }).withMessage('Published year must be a valid number'),

    body('authors')
        .optional()
        .isString().withMessage('Authors must be an array'),

    body('categories')
        .optional()
        .isString().withMessage('Categories must be an array'),
];
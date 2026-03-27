export default function (error, req, res, next) {
    error.statusCode = error.statusCode || 500;
    res.render('err', {message: error.message, status: error.statusCode});
}
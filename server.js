import express from 'express';
import dotenv from 'dotenv';
import morgan from 'morgan';
import mongoose from 'mongoose';
import { connectDb } from './config/dbConfig.js';

// Retrieve All Environment Varaibles
dotenv.config();

// Inistantiate the Server..
const app = express();

// connect to Db
connectDb();

// Storing key-values for storage and for some App reqiured Settings..
app.set('view engine', 'ejs');
app.set('views', './views');
app.set('port', process.env.PORT || 5050);

// Use Global middle-wares <-> applying these middle-wares on all routes..
app.use(morgan('dev')); //? This is important for logging requests.. 
app.use(express.static('public')); //? This is important to serve static files < before checking any routes >..
app.use(express.urlencoded({extended: true})); //? This is important for parsing the [ form Posted data ]..
app.use(express.json()); //? This is important for posting a [ json data ].. 

// Routers

// Fall-out route
app.use((req, res) => {
    res.status(404).send(`<h1>Not-Found</h1>`)
});


// Global Value
const PORT = app.get('port');


// Once The MongoDb is On We start the server..
mongoose.connection.once('open', () => {
    console.log('Connected to MongoDb :D');
    app.listen(PORT, () => {
        const servStatus = `Server Started at PORT ${PORT} :D`
        console.log(servStatus);
    });
})
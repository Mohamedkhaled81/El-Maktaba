import express from 'express';
import dotenv from 'dotenv';
import morgan from 'morgan';
import mongoose from 'mongoose';
import { connectDb } from './config/dbConfig.js';
import methodOverride from 'method-override';
import rootRouter from './routes/index.js';

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

// Global Value
const PORT = app.get('port');

// Use Global middle-wares <-> applying these middle-wares on all routes..
app.use(methodOverride("_method"));
app.use(morgan('dev')); //? This is important for logging requests.. 
app.use(express.static('public')); //? This is important to serve static files < before checking any routes >..
app.use(express.urlencoded({extended: true})); //? This is important for parsing the [ form Posted data ]..
app.use(express.json()); //? This is important for posting a [ json data ].. 

// Routers
app.use('/', rootRouter);

// Once The MongoDb is On We start the server..
mongoose.connection.once('open', () => {
    console.log('Connected to MongoDb :D');
    app.listen(PORT, () => {
        const servStatus = `Server Started at PORT ${PORT} :D`
        console.log(servStatus);
    });
});
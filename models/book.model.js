import mongoose, {Schema} from "mongoose";


/**
 ** Everything in Mongoose starts with a Schema.
 ** Each schema maps to a MongoDB collection
 ** and defines the shape of the documents within that collection.
 */

const bookSchema = new Schema({
    title: {type: String, required: [true, 'Title is required field!'], unique: [true, 'Title Should be unique!']},
    description: {type: String, required: [true, 'Description is required field!']},
    publishedYear: {type: Number, required: [true, 'publishedYear is required field!']},
    authors: [String],
    categories: [String]
});

const book = mongoose.model('Book', bookSchema);

export default book;
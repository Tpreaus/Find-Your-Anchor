//mongoose library
const mongoose = require('mongoose');

// MongoDB connection URI
const dbURI = 'mongodb+srv://clarkep19:clarkep19@fya.pdybubw.mongodb.net/clubs?retryWrites=true&w=majority';

// Connecting to MongoDB
mongoose.connect(dbURI)
  .then(() => console.log('MongoDB connected…'))
  .catch(err => console.error('Connection error:', err));
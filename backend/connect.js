const mongoose = require('mongoose');
const dbURI = 'mongodb+srv://clarkep19:clarkep19@fya.pdybubw.mongodb.net/clubs?retryWrites=true&w=majority';

mongoose.connect(dbURI)
  .then(() => console.log('MongoDB connected…'))
  .catch(err => console.error('Connection error:', err));

const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/clubs')
  .then(() => console.log('MongoDB connected…'))
  .catch(err => console.error('Connection error:', err));


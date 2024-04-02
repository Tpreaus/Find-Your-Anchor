const mongoose = require('mongoose');
const { Schema } = mongoose;

const clubSchema = new Schema({
  "Activity Name": { 
    type: String,
    required: true // assuming every club must have a name
  },
  "Description": {
    type: String,
    required: true // assuming every club must have a description
  }
});

const Club = mongoose.model('Club', clubSchema, 'rollins');

module.exports = Club;

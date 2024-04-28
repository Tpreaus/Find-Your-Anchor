//mongoose library
const mongoose = require('mongoose');

// Defining the schema for Rollins Club
const rollinsClubSchema = new mongoose.Schema({
  "Activity Name": {
    type: String,
    required: true 
  },
  "Description": {
    type: String,
    required: true 
  },
  "Image URL": {  
    type: String,
    required: true  
  }
});

// Creating the RollinsClub model using the schema
const RollinsClub = mongoose.model('RollinsClub', rollinsClubSchema, 'rollinsClubs');

// Exporting the RollinsClub model
module.exports = RollinsClub;
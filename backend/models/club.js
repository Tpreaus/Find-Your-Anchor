const mongoose = require('mongoose');

const rollinsClubSchema = new mongoose.Schema({
  "Activity Name": {
    type: String,
    required: true // Assuming the Activity Name is required
  },
  "Description": {
    type: String,
    required: true // Assuming the Description is also required
  },
  "Image URL": {  // Adding the image URL field
    type: String,
    required: true  // Assuming the image URL might not be required
  }
  // You can add other fields here as needed, following the structure of your documents
});

const RollinsClub = mongoose.model('RollinsClub', rollinsClubSchema, 'rollinsClubs');

module.exports = RollinsClub;
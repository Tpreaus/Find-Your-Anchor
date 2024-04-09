// models/RollinsClub.js
const mongoose = require('mongoose');

const rollinsClubSchema = new mongoose.Schema({
  // Adjusting the schema to match the document structure
  // Note: Mongoose will automatically handle the _id field, so you don't need to explicitly define it unless you have specific requirements.
  "Activity Name": {
    type: String,
    required: true // Assuming the Activity Name is required
  },
  "Description": {
    type: String,
    required: true // Assuming the Description is also required
  }
  // You can add other fields here as needed, following the structure of your documents
});

const RollinsClub = mongoose.model('RollinsClub', rollinsClubSchema, 'rollinsClubs');

module.exports = RollinsClub;

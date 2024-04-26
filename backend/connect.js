const mongoose = require('mongoose');
const dbURI = 'mongodb+srv://clarkep19:clarkep19@fya.pdybubw.mongodb.net/';

// Create a connection to the MongoDB database
const dbConnection = mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true });

// Event listeners for the MongoDB connection
mongoose.connection.on('connected', () => {
  console.log('MongoDB connected...');
});

mongoose.connection.on('error', (err) => {
  console.error('Connection error:', err);
});

mongoose.connection.on('disconnected', () => {
  console.log('MongoDB disconnected...');
});

// Export the database connection
module.exports = dbConnection;

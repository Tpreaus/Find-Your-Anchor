const express = require('express');
const app = express();
const clubRoutes = require('./routes/clubRoutes.js');
const aiRoutes = require('./routes/aiRoutes.js');
const PORT = process.env.PORT || 3005;
const cors = require('cors'); // Import the cors package

app.use(cors()); // Enable CORS for all routes


// Require connect.js here if necessary
require('./connect.js'); // Assuming this file establishes database connection

// Middleware
app.use(express.json()); // Parse JSON request bodies

// Mount Routes under '/api'
app.use('/api', clubRoutes); // All routes in clubRoutes will be prefixed with '/api'
app.use('/api', aiRoutes); // All routes in aiRoutes will be prefixed with '/api'


// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

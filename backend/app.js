const express = require('express');
const app = express();
const clubRoutes = require('./routes/clubRoutes.js')
const PORT = process.env.PORT || 3002;

// Require connect.js here
require('./connect.js');

// Other middleware and routing setup
app.use(express.json());    

app.use('/', clubRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

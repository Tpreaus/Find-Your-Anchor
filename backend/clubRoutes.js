const express = require('express');
const router = express.Router();
const Club = require('../models/Club'); // Assuming 'Club' is your Mongoose model

// Retrieve all clubs
router.get('/clubs', async (req, res) => {
  try {
    const clubs = await club.find();
    res.json(clubs);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;

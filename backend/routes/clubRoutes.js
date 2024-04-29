const express = require('express');
const router = express.Router();
const clubController = require('../controllers/clubcontroller.js');

router.get('/clubs', clubController.getAllClubs); // Get all clubs

module.exports = router;

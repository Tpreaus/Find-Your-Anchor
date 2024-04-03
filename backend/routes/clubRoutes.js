const express = require('express');
const router = express.Router();
const clubController = require('../controllers/clubController.js');

router.get('/clubs', clubController.getAllClubs); // Get all clubs
router.post('/clubs', clubController.addClub); // Add a new club

// Placeholder for other routes
// router.get('/clubs/:id', clubController.getClubById);
// router.put('/clubs/:id', clubController.updateClub);
// router.delete('/clubs/:id', clubController.deleteClub);

module.exports = router;
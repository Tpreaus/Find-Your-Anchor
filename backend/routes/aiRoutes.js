const express = require('express');
const router = express.Router();
const aiController = require('../controllers/aiController.js');


router.post('/ai', aiController.runAi); // Run AI


module.exports = router;
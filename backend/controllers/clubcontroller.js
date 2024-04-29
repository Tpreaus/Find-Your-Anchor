const RollinsClub = require('../models/club');

// Fetch all clubs
exports.getAllClubs = async (req, res) => {
  try {
    console.log(RollinsClub); // Log RollinsClub object to check if it's defined
    const clubs = await RollinsClub.find();
    res.json(clubs); // Sends all clubs as JSON including Image URL
  } catch (error) {
    // Consistently send errors as JSON
    res.status(500).json({ message: "Error fetching clubs", error: error.message });
  }
}



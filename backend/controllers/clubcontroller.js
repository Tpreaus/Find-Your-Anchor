const Club = require('../models/club.js'); // Ensure the path matches the location of your model file

// Fetch all clubs
exports.getAllClubs = async (req, res) => {
  try {
    const clubs = await Club.find();
    res.json(clubs); // Sends all clubs as JSON
  } catch (error) {
    // Consistently send errors as JSON
    res.status(500).json({ message: "Error fetching clubs", error: error.message });
  }
};

// Add a new club
exports.addClub = async (req, res) => {
  try {
    const newClub = new Club({
      "Activity Name": req.body["Activity Name"],
      "Description": req.body.Description,
    });

    const savedClub = await newClub.save();
    res.status(201).json(savedClub); // Send the saved club as JSON
  } catch (error) {
    // Consistently send errors as JSON
    res.status(400).json({ message: "Error adding new club", error: error.message });
  }
};

// Placeholder for other CRUD operations
// exports.getClubById = async (req, res) => { ... };
// exports.updateClub = async (req, res) => { ... };
// exports.deleteClub = async (req, res) => { ... };

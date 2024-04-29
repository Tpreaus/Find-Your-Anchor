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

exports.getClubById = async (req, res) => {
  try {
    const clubId = req.params.id;
    const club = await RollinsClub.findById(clubId);
    res.json(club);
  } catch (error) {
    res.status(500).json({ message: "Error fetching club", error: error.message });
  }
}


// Add a new club
exports.addClub = async (req, res) => {
  try {
    const { ActivityName, Description, ImageURL } = req.body;

    const newClub = new RollinsClub({
      "Activity Name": ActivityName,
      "Description": Description,
      "Image URL": ImageURL
    });

    const savedClub = await newClub.save();
    res.status(201).json(savedClub); // Send the saved club as JSON
  } catch (error) {
    // Consistently send errors as JSON
    res.status(400).json({ message: "Error adding new club", error: error.message });
  }
}


const RollinsClub = require('../models/club.js');

// Fetch all clubs
exports.getAllClubs = async (req, res) => {
  try {
    const clubs = await RollinsClub.find();
    res.json(clubs); // Sends all clubs as JSON including Image URL
  } catch (error) {
    // Consistently send errors as JSON
    res.status(500).json({ message: "Error fetching clubs", error: error.message });
  }
};

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
};

exports.clubMatch = async (req, res) => {
  const { spawn } = require('child_process');
  let pythonOutput = '';

  // The string to pass to the Python script
  let myString = req.query.myString;

// Run the Python script and pass the string as an argument
const python = spawn('python', ['../ai/openAi.py', myString]);

  // Listen for data from the script's stdout
  python.stdout.on('data', (data) => {
    pythonOutput += data.toString();
  });

  // Listen for data from the script's stderr
  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  // Handle the script's close event
  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    // Send the Python script's output in the HTTP response
    res.send(pythonOutput);
  });
};


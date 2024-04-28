const { exec } = require('child_process');

exports.runAi = async (req, res) => {
    const { inputData } = req.body; // Assuming input data is sent in the request body

    // Command to run the Python script with input data as argument
    const command = `python3 ai/openAi.py ${inputData}`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing Python script: ${error}`);
            return res.status(500).json({ error: 'Internal server error' });
        }
        console.log(`Python script output: ${stdout}`);
        res.json({ output: stdout });
    });
}
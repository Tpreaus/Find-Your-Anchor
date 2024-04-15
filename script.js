

// Function to toggle visibility of time input fields
function toggleTimeInputs() {
    var variableTimeSelect = document.getElementById('variable-time-select');
    var timeInputsContainer = document.getElementById('time-inputs');

    if (variableTimeSelect.value === 'variable-time') {
        timeInputsContainer.innerHTML = `
            <div class="form-group">
                <label for="monday-time">Monday Time:</label>
                <input type="time" id="monday-time" name="monday-time">
            </div>
            <!-- Repeat for other days -->
        `;
    } else {
        timeInputsContainer.innerHTML = ''; // Clear the time inputs
    }
}

// Event listener for variable time select
document.getElementById('variable-time-select').addEventListener('change', toggleTimeInputs);

// Initially toggle based on the select value
toggleTimeInputs();

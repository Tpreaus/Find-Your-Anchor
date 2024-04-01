const autocompleteSelect = document.getElementById('autocompleteSelect');
const autocompleteOptions = document.getElementById('autocompleteOptions');

// Sample data source (replace with your actual data)
const data = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven'];

// Function to filter the data source based on user input
function filterData(value) {
  const filteredData = data.filter(item =>
    item.toLowerCase().includes(value.toLowerCase())
  );
  return filteredData.sort(); // Sort the filtered data alphabetically
}

// Function to display the autocomplete options
function showOptions(options) {
  autocompleteOptions.innerHTML = '';
  options.forEach(option => {
    const optionElement = document.createElement('div');
    optionElement.innerHTML = option;
    optionElement.addEventListener('click', () => {
      const newOption = document.createElement('option');
      newOption.value = option;
      newOption.text = option;
      autocompleteSelect.add(newOption, null);
      autocompleteSelect.value = option;
      autocompleteOptions.innerHTML = '';
    });
    autocompleteOptions.appendChild(optionElement);
  });
}

// Event listener for select element
autocompleteSelect.addEventListener('input', () => {
  const inputValue = autocompleteSelect.value;
  if (inputValue) {
    const filteredOptions = filterData(inputValue);
    showOptions(filteredOptions);
  } else {
    autocompleteOptions.innerHTML = '';
  }
});

// Event listener for clicking outside the autocomplete options
document.addEventListener('click', (event) => {
  if (!autocompleteOptions.contains(event.target)) {
    autocompleteOptions.innerHTML = '';
  }
});
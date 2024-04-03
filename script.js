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



// add club box as more are added
document.addEventListener('DOMContentLoaded', function() {
  // Assuming your club's data is in an array of objects like this:
  const clubs = [
      {
          name: "Club Tennis",
          meetingDays: "Tue & Thu",
          meetingTime: "7:00pm - 8:30pm",
          imageUrl: "assets/priscilla-du-preez-ZkR9yT1cR7g-unsplash.jpg"
      },
      // Add more clubs here...
  ];

  // Select the container where you want to append the clubs
  const clubsContainer = document.getElementById('clubsContainer');


  // Function to create a club card
  function createClubCard(club) {
      const colDiv = document.createElement('div');
      colDiv.classList.add('col');

      const cardDiv = document.createElement('div');
      cardDiv.classList.add('card', 'card-cover', 'h-100', 'overflow-hidden', 'text-bg-dark', 'rounded-4', 'shadow-lg');
      cardDiv.style.backgroundImage = `url(${club.imageUrl})`;

      const contentDiv = document.createElement('div');
      contentDiv.classList.add('d-flex', 'flex-column', 'h-100', 'p-5', 'pb-3', 'text-white', 'text-shadow-1');

      const titleH3 = document.createElement('h3');
      titleH3.classList.add('pt-5', 'mt-5', 'mb-4', 'display-6', 'lh-1', 'fw-bold');
      titleH3.textContent = club.name;

      const ul = document.createElement('ul');
      ul.classList.add('d-flex', 'list-unstyled', 'mt-auto');

      const liDays = document.createElement('li');
      liDays.classList.add('d-flex', 'align-items-center', 'me-3');
      liDays.innerHTML = `<i class="ri-calendar-schedule-line"></i><small>${club.meetingDays}</small>`;

      const liTime = document.createElement('li');
      liTime.classList.add('d-flex', 'align-items-center');
      liTime.innerHTML = `<i class="ri-time-line"></i><small>${club.meetingTime}</small>`;

      ul.appendChild(liDays);
      ul.appendChild(liTime);

      contentDiv.appendChild(titleH3);
      contentDiv.appendChild(ul);

      cardDiv.appendChild(contentDiv);
      colDiv.appendChild(cardDiv);

      return colDiv;
  }

  // Loop through clubs and append each one to the container
  clubs.forEach(club => {
      const clubCard = createClubCard(club);
      clubsContainer.appendChild(clubCard);
  });
});

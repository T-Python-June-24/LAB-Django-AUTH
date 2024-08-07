document.addEventListener('DOMContentLoaded', function () {
  const dropdownButton = document.querySelector('.dropdown-button');
  const dropdownMenu = document.querySelector('.dropdown-menu');

  dropdownButton.addEventListener('click', function (event) {
      // Toggle the dropdown menu's visibility
      dropdownMenu.classList.toggle('hidden');
      event.stopPropagation(); // Prevent the click event from bubbling up
  });

  // Close the dropdown if clicking outside of it
  document.addEventListener('click', function (event) {
      if (!dropdownMenu.contains(event.target) && !dropdownButton.contains(event.target)) {
          dropdownMenu.classList.add('hidden');
      }
  });
});
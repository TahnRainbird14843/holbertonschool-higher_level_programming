const header = document.querySelector('header');
const colDiv = document.querySelector('#toggle_header');

colDiv.addEventListener ('click', () => {
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});

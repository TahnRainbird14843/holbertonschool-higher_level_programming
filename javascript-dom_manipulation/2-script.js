const header = document.querySelector('header');
const redDiv = document.querySelector('#red_header');

redDiv.addEventListener ('click', () => {
  header.classList.add('red');
});

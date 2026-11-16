const header = document.querySelector('header');
const updDiv = document.querySelector('#update_header');

updDiv.addEventListener ('click', () => {
  header.textContent = 'New Header!!!';
});

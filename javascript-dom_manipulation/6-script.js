const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const charDiv = document.querySelector('#character');

fetch(url)
  .then(response => response.json())
  .then(data => charDiv.textContent = data)
  .catch(error => console.error(error));

const { createElement } = require("react")

const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
const movieList = document.querySelector('#list_movies')

fetch(url)
  .then(response => response.json())
  .then(data => {
    data.results.forEach(film => {
        const li = document.createElement('li');
        li.textContent = film.title;
        movieList.appendChild(li);
    });
  })
  .catch(error => console.error(error));
  
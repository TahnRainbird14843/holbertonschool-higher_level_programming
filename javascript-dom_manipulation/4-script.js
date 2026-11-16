const addDiv = document.querySelector('#add_item');
const ulList = document.querySelector('.my_list');

addDiv.addEventListener ('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ulList.appendChild(li)
});

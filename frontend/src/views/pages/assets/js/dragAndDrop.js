function dragAndDrop() {
  var toDo = document.querySelector('#toDo');
  var inProgress = document.querySelector('#inProgress');
  var done = document.querySelector('#done');

  new Sortable(toDo, {
    group: 'shared',
    animation: 150,
  });

  new Sortable(inProgress, {
    group: 'shared',
    animation: 150,
  });

  new Sortable(done, {
    group: 'shared',
    animation: 150,
  });
}

export default dragAndDrop;

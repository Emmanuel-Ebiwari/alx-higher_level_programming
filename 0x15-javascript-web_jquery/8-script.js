$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done(function (data) {
    let titles = data.results;
    for (let i = 0; i < titles.length; i++) {
      $('UL#list_movies').append('<li>' + titles[i].title + '</li>');
    }
  });

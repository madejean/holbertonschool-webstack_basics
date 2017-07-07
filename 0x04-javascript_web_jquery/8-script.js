$(function() {
  $.get("http://swapi.co/api/films?format=json", function(data, status) {
    $.each(data.results, function(index) {
      $("#list_movies").append("<li>" + data.results[index].title + "</li>")
    })
  })
})

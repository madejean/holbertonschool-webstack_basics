$(function() {
  $.get("http://swapi.co/api/people/5/?format=json", function(data, status) {
    $("#character").text(data.name)
  })
})

document.addEventListener('DOMContentLoaded', function() {
  $("#btn_search").click(function() {
    let userval = $("#city_search").val()
    $.get("https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:" + userval + "%22)&format=json", function(data, status) {
      $("#wind_speed").text(data.query.results.channel.wind.speed)
    })
  })
})

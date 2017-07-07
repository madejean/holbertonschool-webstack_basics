document.addEventListener('DOMContentLoaded', function() {
  $("#add_item").click(function() {
    $("ul.my_list").append("<li>Item</li>")
  });

  $("#remove_item").click(function() {
    $(".my_list :last").remove()
  });

  $("#clear_list").click(function() {
    $(".my_list li").remove()
  });
}, false);

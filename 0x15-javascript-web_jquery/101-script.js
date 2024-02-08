$(document).ready(function(){

    $(document).on("click", "#add_item", function() {
        $(".my_list").append("<li>Item</li>");
    });

    $(document).on("click", "#remove_item", function() {
        $(".my_list li:last-child").remove();
    });

    $(document).on("click", "#clear_list", function() {
        $(".my_list").empty();
    });

});
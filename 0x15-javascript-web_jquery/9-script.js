$(document).ready(function() {

    $.ajax({
        type: "GET",
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",

        success: (greeting) => {
            $("#hello").text(greeting.hello);
        }
    })

});
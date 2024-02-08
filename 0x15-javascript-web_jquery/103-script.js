$(document).ready(function() {

    $("#language_code").keypress(function (key) {
        if(key.which == 13) {
           $("#btn_translate").click();
           return false;  
        }
    }); 

    $(document).on("click", "#btn_translate", function() {
        const languageCode = $("#language_code").val();
        $.ajax({
            type: "GET",
            url: `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,

            success: (greeting) => {
                $("#hello").html(greeting.hello);
                $("#language_code").val("");
            }
        });
    });

});
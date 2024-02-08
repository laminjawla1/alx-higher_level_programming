$(document).ready(function() {

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
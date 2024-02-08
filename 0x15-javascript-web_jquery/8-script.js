$(document).ready(function() {

    const $movies = $("#list_movies");

    $.ajax({
        type: "GET",
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",

        success: function(films) {
            $.each(films.results, function(i, film) {
                $movies.append(`<li>${film.title}</li>`);
            })
        }
    });

});
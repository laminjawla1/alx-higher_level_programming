$(document).ready(() => {
    $(document).on("click", "#toggle_header", () => {
        const currentClass = $("header").attr("class");
        if (currentClass === "red")
            $("header").removeClass("red").addClass("green");
        else
            $("header").removeClass("green").addClass("red");
    });
});
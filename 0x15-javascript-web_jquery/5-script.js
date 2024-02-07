$(document).ready(() => {
    $(document).on("click", "#add_item", () => {
        $(".my_list").append("<li>Item</li>");
    });
});
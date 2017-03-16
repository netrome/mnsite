/**
 * Created by marten on 2017-01-23.
 */

$(document).ready(function(){

    //$("input, textarea").attr("class", "w3-input");

    $("#change").click(function() {
        var data = {question: "blank"};
        $("#dish").load("/foodlist/ajax/", data);
    });

    $(".dish-container").click(function () {
        var name = $(this).children("h3").text();

        data = {name: name};
        $("#outer_form_holder").load("/foodlist/ajax_form/", data);
    });

});
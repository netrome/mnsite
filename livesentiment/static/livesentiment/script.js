/**
 * Created by marten on 2018-01-04.
 */

white_star = "☆";
filled_star= "★";

function getStarts(rating) {
    stars = "";
    i = 0;
    while (i < rating){
        stars += filled_star;
        i += 1;
    }

    while (stars.length < 5){
        stars += white_star;
    }
    return stars
}

$(document).ready(function(){

    $("input, textarea").attr("class", "w3-input");  // De-uglify inputs

    allow_request = true;  // Timeout since our simple server can't handle too many requests

    $("#update").click(function () {
        data = $("#textform").serializeArray();
        text = data[1].value;
        data = {text: text};
        if (allow_request) {
            console.log("Event ---");
            $("#response_text").load("/livesentiment/get_value/", data);
            rating = Math.round(parseFloat($("#response_text").text().split(":")[1]));
            console.log(rating);
            console.log(getStarts(rating));
            $("#stars").text(getStarts(rating));
            allow_request = false;
            window.setTimeout(function () {
                allow_request = true;
            }, 1000);
        }
    });

    $("#textform").keyup(function (e) {
        data = $("#textform").serializeArray();
        text = data[1].value;
        data = {text: text};
        if (allow_request && (e.which == 13 || e.which == 32 || e.which == 190)) {
            console.log("Event ---");
            $("#response_text").load("/livesentiment/get_value/", data);
            rating = Math.round(parseFloat($("#response_text").text().split(":")[1]));
            console.log(rating);
            console.log(getStarts(rating));
            $("#stars").text(getStarts(rating));
            allow_request = false;
            window.setTimeout(function () {
                allow_request = true;
            }, 1000);
        }
    });

    $("#response_text").click(function () {
        data = $("#textform").serializeArray();
        text = data[1].value;
        data = {text: text};
        $("#response_text").load("/livesentiment/get_value/", data);
    });

    $("h1").click(function () {
        $("#response_text").fadeToggle();
    });

});

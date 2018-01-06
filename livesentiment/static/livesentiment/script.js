/**
 * Created by marten on 2018-01-04.
 */

$(document).ready(function(){

    $("input, textarea").attr("class", "w3-input");  // De-uglify inputs

    allow_request = true;  // Timeout since our simple server can't handle too many requests

    $("#update").click(function () {
        if (allow_request) {
            console.log("Event ---");
            $("#response_text").load("/livesentiment/get_value/", data);
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

});

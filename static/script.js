function getBotResponse() {

    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText alert"><span>' + rawText + ' <i class="bi bi-person-hearts"></i></span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    
    $.get("/get", { msg: rawText }).done(function(data) {
        var botHtml = '<p class="botText alert"><span><i class="bi bi-robot"></i> ' + data + "</span></p>";
        $("#chatbox").append(botHtml);
        document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    });
}

$("#textInput").keypress(function(e) {
    if (e.which == 13) {
        getBotResponse();
    }
});
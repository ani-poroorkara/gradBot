function getResponse() {
    let userText = $("#textInput").val();
    let userHtml = '<p class="userText alert"><span>' + userText + ' <i class="bi bi-person-hearts"></i></span></p>';
    
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    
    $.get("/get", { msg: userText }).done(function(data) {
        var botHtml = '<p class="botText alert"><span><i class="bi bi-robot"></i> ' + data + "</span></p>";
        $("#chatbox").append(botHtml);
        document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    });
}

$("#textInput").keypress(function(e) {
//if enter key is pressed
    if(e.which == 13) {
        getResponse();
    }
});
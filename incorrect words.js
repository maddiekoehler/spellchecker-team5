function getRedLines (incorrectWords, cursorPosition){
    console.log('cursorPosition',cursorPosition);
    var newHTML = "";
    $('#input').text().replace(/[\s]+/g, " ").trim().split(" ").forEach(function(val, idx){
            let newVal = val.replace(/[^\w\s]/gi, '')

        if (incorrectWords.indexOf(val.trim()) > -1)
            newHTML += "<span id='"+incorrectWords.indexOf(val.trim())+"'class='red_line'>" + val + "&nbsp;</span>";
        else
            newHTML += ""+val+" "; 
    });
    $('#input').html(newHTML);
    $('#input').focusEnd();
}
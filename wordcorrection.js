document.body.onkeyup = function(e){
    if(e.keyCode == 32){
        console.log('keyboard pressed', document.getElementById("input").innerText);
        var spellText = document.getElementById("input").innerText;
        console.log('spellText',spellText);
        
        if(spellText != '' && spellText != null)
            sendText(spellText); 
    }
}
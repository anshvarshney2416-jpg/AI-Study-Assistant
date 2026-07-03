const form = document.getElementById("chatForm");
const loading = document.getElementById("loading");
const chatBox = document.getElementById("chatBox");

if(form){
    form.addEventListener("submit", function(){
        loading.style.display = "block";
    });
}

if(chatBox){
    chatBox.scrollTop = chatBox.scrollHeight;
}

function clearChat(){
    window.location.href = "/clear";
}
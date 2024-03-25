async function sendMessage() {
    var userInput = document.getElementById("user-input").value.trim();
    var chatBox = document.getElementById("chat-box");
    var userTextbox = document.getElementById("user-input");
    var sendBtn = document.getElementById("send-btn");

    if (userInput === "") return;

    // Disable user input and send button during loading
    userTextbox.disabled = true;
    sendBtn.disabled = true;

    // Clear user input
    userTextbox.value = "";

    // Display user message
    chatBox.innerHTML += '<p style="text-align: right;">' + userInput + '</p>';
    chatBox.scrollTop = chatBox.scrollHeight;

    // Display loading state
    chatBox.innerHTML += '<p class="loading" style="text-align: left;">Loading</p>';
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send user message to API
    var response = await fetch('http://127.0.0.1:8000/chat/?msg='+userInput, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    // Get API response
    //var data = await response.json();
    var botResponse = await response.json();

    // Display API response
    chatBox.innerHTML += '<p style="text-align: left;">' + botResponse + '</p>';
    chatBox.innerHTML += '<hr>'
    chatBox.scrollTop = chatBox.scrollHeight;

    // Enable user input and send button after response received
    userTextbox.disabled = false;
    sendBtn.disabled = false;
}

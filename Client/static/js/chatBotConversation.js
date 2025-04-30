// Selecting elements for interaction
var chatBotSession = document.querySelector(".chatBot .chatBody .chatSession");
var chatBotSendButton = document.querySelector(".chatBot .chatForm #sendButton");
var chatBotTextArea = document.querySelector(".chatBot .chatForm #chatTextBox");

// Bot initial and error messages
var chatBotInitiateMessage = "Hello! I am ChatBot.";
var chatBotBlankMessageReply = "Type something!";


// Function to handle user input and bot reply
function handleSendMessage() {
    var userInput = chatBotTextArea.value.trim();

    if (userInput) {
        // Append user's message
        createContainer("message", userInput);

        // Simulate bot's response
        fetch('/get?msg=' + encodeURIComponent(userInput), {
            method: 'GET'
        })
            .then(response => response.json())
            .then(data => {
                data.forEach((botMessage) => {
                    createContainer("reply", botMessage.text, 'bot');
                });
            })
            .catch(() => {
                createContainer("reply", "There was an error communicating with the bot. Please try again.", 'bot');
            });
    } else {
        // Append error message
        createContainer("reply", chatBotBlankMessageReply, 'bot');
    }

    // Clear the text area
    chatBotTextArea.value = "";
    chatBotTextArea.focus();
}

function createContainer(typeOfContainer, messageContent, sender) {
    var containerClass = typeOfContainer === "message" ? "message" : "reply";

    // Create a new container
    var newContainer = document.createElement("div");
    newContainer.classList.add("container", containerClass);

    // Add avatar image
    var img = document.createElement('img');
    img.classList.add('chat-avatar');
    img.src = sender === 'bot' ? 'static/img/chtrobo.png' : 'static/img/momuser.png';
    newContainer.appendChild(img);

    // Add message content
    // var newParagraph = document.createElement("p");
    const textDiv = document.createElement('div'); // Create a new div to hold the HTML content.
    textDiv.classList.add(containerClass, "animateChat", "message-text");

    // isHTML || messageContent.includes('<br>') || messageContent.includes('href=') || messageContent.includes('img src=')

    if (messageContent.includes("<") || messageContent.includes(">") || messageContent.includes('<br>') || messageContent.includes('href=') || messageContent.includes('img src=')) {
        // Handle HTML content
        textDiv.innerHTML = messageContent;
    } else {
        // Handle plain text
        textDiv.textContent = messageContent;
    }

    newContainer.appendChild(textDiv);

    // Append the container to the chat session
    chatBotSession.appendChild(newContainer);
    newContainer.scrollIntoView({ behavior: "smooth" });
}

// Event listener for the send button
chatBotSendButton.addEventListener("click", (event) => {
    event.preventDefault();
    handleSendMessage();
});

// Event listener for the Enter key
chatBotTextArea.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault(); // Prevent default behavior of adding a newline
        handleSendMessage();
    }
});

// Initialize the conversation
function initiateConversation() {
    // Add avatar image

    chatBotSession.innerHTML = "";
    createContainer("reply", chatBotInitiateMessage);
}


// Start the bot
initiateConversation();



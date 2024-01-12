async function sendMessage() {
  const userInput = document.getElementById('user-input');
  const message = userInput.value.trim();

  if (message !== '') {
    appendMessage('user', message);
    try {
      const payload = {
        "sender": "test_user",
        "message": message
      };
      const response = await axios.post("http://localhost:5005/webhooks/rest/webhook", payload);
      if (response.data) {
        appendMessage('response', response.data[0].text);
      } else {
        appendMessage('response', "something went wrong! Please try again later");
      }
    } catch (err) {
      console.log(err);
    }
    userInput.value = '';
  }
}

function appendMessage(sender, data) {
  const chatbotMessages = document.getElementById('chatbot-messages');
  const messageElement = document.createElement('div');
  if (sender === 'user') messageElement.classList.add('message');
  else if (sender === 'response') messageElement.classList.add('response');
  messageElement.innerText = data;
  chatbotMessages.appendChild(messageElement);
  chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function toggleChatbot() {
  const chatbotContainer = document.querySelector('.chatbot-container');
  chatbotContainer.classList.toggle('closed');
}

function handleKeyDown(event) {
  event = event || window.event; // Add this line to handle different browser implementations
  if (event.key === 'Enter') {
    sendMessage();
  }
}

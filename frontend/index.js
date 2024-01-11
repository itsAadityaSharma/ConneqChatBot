function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();
  
    if (message !== '') {
      appendMessage('user', message);
      // Here you can implement your logic to handle user input
      // For demo, let's just clear the input field
      userInput.value = '';
    }
  }
  
  function appendMessage(sender, message) {
    const chatbotMessages = document.getElementById('chatbot-messages');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.innerText = message;
    chatbotMessages.appendChild(messageElement);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
  }
  
  function toggleChatbot() {
    const chatbotContainer = document.querySelector('chatbot-container');
    chatbotContainer.classList.toggle('closed');
  }
  function handleKeyDown(event) {
    if (event.key === 'Enter') {
      sendMessage();
    }
  }
  
  
function sendMessage() {

  const input = document.getElementById("userInput");
  const message = input.value.trim();

  if (message === "") {
    return;
  }

  const messages = document.getElementById("messages");

  const userDiv = document.createElement("div");
  userDiv.className = "message user-message";
  userDiv.innerText = message;

  messages.appendChild(userDiv);

  const botDiv = document.createElement("div");
  botDiv.className = "message bot-message";
  botDiv.innerText = "Typing...";

  messages.appendChild(botDiv);

  messages.scrollTop = messages.scrollHeight;

  setTimeout(() => {
    botDiv.innerText = "You said: " + message;

    messages.scrollTop = messages.scrollHeight;
  }, 1000);

  input.value = "";
}
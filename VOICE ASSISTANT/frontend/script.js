document.addEventListener("DOMContentLoaded", () => {
  const micButton = document.querySelector(".microphone-btn");
  const sendButton = document.querySelector(".send-btn");
  const inputBox = document.querySelector(".text-input");

  // 🔊 Voice Input
  micButton.addEventListener("click", () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = async (event) => {
      const command = event.results[0][0].transcript;
      inputBox.value = command; // Show it in the text box
      processCommand(command); // Send to Python
    };
  });

  // 💬 Text Input
  sendButton.addEventListener("click", () => {
    const command = inputBox.value.trim();
    if (command.length > 0) {
      processCommand(command); // Send to Python
    }
  });

  // 🔁 Common function to call Python
  async function processCommand(command) {
    const response = await eel.handle_voice_command(command)(); // Call backend
    showResponse(command, response); // Show both input & output
  }

  function showResponse(input, response) {
    const outputDiv = document.createElement("div");
    outputDiv.innerHTML = `
      <p><strong>You:</strong> ${input}</p>
      <p><strong>Assistant:</strong> ${response}</p>
      <hr />
    `;
    document.body.appendChild(outputDiv);
  }
});

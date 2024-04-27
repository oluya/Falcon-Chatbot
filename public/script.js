// script.js
document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const signupBtn = document.getElementById('signupBtn');
    const signupForm = document.getElementById('signupForm');
    const loginForm = document.getElementById('loginForm');
    const switchLogin = document.getElementById('switchLogin');
    const switchSignup = document.getElementById('switchSignup');
  
    const toggleForms = () => {
      if (signupForm.style.display === 'none') {
        signupForm.style.display = 'block';
        loginForm.style.display = 'none';
        signupBtn.classList.add('active');
        loginBtn.classList.remove('active');
      } else {
        signupForm.style.display = 'none';
        loginForm.style.display = 'block';
        loginBtn.classList.add('active');
        signupBtn.classList.remove('active');
      }
    };
  
    loginBtn.addEventListener('click', toggleForms);
    signupBtn.addEventListener('click', toggleForms);
    switchLogin.addEventListener('click', toggleForms);
    switchSignup.addEventListener('click', toggleForms);
  
    // Initialize with signup form active
    signupForm.style.display = 'block';
});

document.getElementById('startChatBtn').addEventListener('click', function() {
    alert('Chat Started!');
    // Here you can add further logic to handle the chat start event
});

// Add click event to each chat example
document.querySelectorAll('.chat-example').forEach(item => {
    item.addEventListener('click', function() {
      let messageInput = document.getElementById('messageInput');
      messageInput.value = this.textContent.replace('Example: "', '').slice(0, -1); // Removes the 'Example: ' prefix and the closing quote
      // Optionally, you could automatically start the chat after clicking the example
      // sendMessage(messageInput.value);
    });
});

  // Code to redirect to the home html
  document.getElementById('loginForm').addEventListener('submit', function(e) {
    //e.preventDefault();  // Prevent the normal form submission
    
    var formData = new FormData(this);
    
    fetch('/login', {
      method: 'POST',
      body: formData
    }) 
    .then(response => response.json())
    .then(data => {
      if (data.status === "success") {
        window.location.href = data.redirect;  // Redirect to the given URL
      } else {
        alert('Login failed!');
      }
    })
    .catch(error => console.error('Error:', error));
});

// First, select all the elements with the class 'chat-example'
const chatExamples = document.querySelectorAll('.chat-example');

// Then, add a click event listener to each chat example
chatExamples.forEach(example => {
  example.addEventListener('click', () => {
    // Copying content to clipboard
    navigator.clipboard.writeText(example.textContent.replace('Example: "', '').slice(0, -1));
    alert(`You clicked on: ${example.textContent}`);
    
  });
});


//Code to logout when the button is clicked.
document.getElementById('logoutButton').addEventListener('click', function() {
  fetch('/logout')
  .then(response => {
      if (response.ok) {
          window.location.href = '/index.html';  // Redirect to index.html on successful logout
      } else {
          alert('Failed to log out. Please try again.');
      }
  })
  .catch(error => console.error('Error logging out:', error));
});





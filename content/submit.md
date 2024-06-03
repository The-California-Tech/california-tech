---
title: Submit an Article to The Tech
authorbox: false
sidebar: "true"
---

  <style>
    #confirmationMessage {
      display: none;
    }
    #loadingMessage {
      display: none;
    }
    #submitButton:disabled {
      background-color: gray;
      cursor: wait;
    }
  </style>
  <div id="formContainer">
    <p>Please fill out the form below to submit your article. A Google Doc will be created automatically using the title you provide. This document will be shared with you for editing and with our editorial team at The California Tech. You will receive an email with a link to the document once it is created.</p>
    <form id="submissionForm">
      <label for="name">Your Name:</label>
      <input type="text" id="name" name="name" required><br><br>
      <label for="email">Your Caltech Email:</label>
      <input type="email" id="email" name="email" required><br><br>
      <label for="title">Article Title:</label>
      <input type="text" id="title" name="title" required><br><br>
      <button type="button" id="submitButton" onclick="submitForm()">Submit Article</button>
    </form>
    <div id="loadingMessage">
      <p>Creating your document, please wait...</p>
    </div>
  </div>
  <div id="confirmationMessage">
    <h2>Submission Successful</h2>
    <p>Your article submission has been created. You will receive an email with the link to your document shortly. You can also access your document <a id="docLink" href="#" target="_blank">here</a>.</p>
  </div>

<script>
    function validateEmail(email) {
      var emailPattern = /^[a-zA-Z0-9._%+-]+@caltech\.edu$/;
      return emailPattern.test(email);
    }

    function submitForm() {
      var name = document.getElementById('name').value;
      var email = document.getElementById('email').value;
      var title = document.getElementById('title').value;
      var submitButton = document.getElementById('submitButton');
      var loadingMessage = document.getElementById('loadingMessage');

      if (email && validateEmail(email)) {
        submitButton.disabled = true;
        submitButton.textContent = 'Creating your document, please wait...';

        var webAppUrl = 'https://script.google.com/macros/s/AKfycbxCpDuLEvVQxKPXGAahakw3RuiWvXWJt7TrPonk288P7-RT9vW3Gp-10ewQSf99gi0ETg/exec' + '?name=' + encodeURIComponent(name) + '&email=' + encodeURIComponent(email) + '&title=' + encodeURIComponent(title);
        fetch(webAppUrl)
          .then(response => response.text())
          .then(data => {
            document.getElementById('formContainer').style.display = 'none';
            document.getElementById('confirmationMessage').style.display = 'block';
            var docLink = document.getElementById('docLink');
            docLink.href = data;
            docLink.textContent = data;
          })
          .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
            submitButton.disabled = false;
            submitButton.textContent = 'Submit Article';
          });
      } else {
        alert('Please enter a valid Caltech email address.');
      }
    }
  </script>
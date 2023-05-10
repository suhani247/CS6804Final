document.addEventListener('DOMContentLoaded', function() {
  function checkText2(text) {
    // Replace with the URL of your external API & any required API key.
    const apiURL = 'https://your-api-url.com/checktext?text=' + encodeURIComponent(text);

    fetch(apiURL)
      .then((response) => response.json())
      .then((data) => {
        if (data.result === 'yes') {
          if (!confirm('Are you sure you want to post this?')) {
            return false;
          }
        }
        return true;
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  function checkText(text) {
   const url = "http://127.0.0.1:8088/gptdetect/";
   const data = {"text":text}
   
    fetch(url, {
  	method: 'POST',
  	headers: {
    		'Content-Type': 'application/json'
	},
	body: JSON.stringify(data)
   })
  .then(response => response.json())
  .then(data => {
  	if(data ==='yes') {
  	 const userConfirmation = confirm("Are you aure you want to post this? Cyberbullying detected");
  	}
    console.log('Success:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
  }
  

  function onInput(event) {
    if (event.target.tagName.toLowerCase() === 'input' || event.target.tagName.toLowerCase() === 'textarea') {
      checkText(event.target.value);
    }
  }

  document.body.addEventListener('input', onInput);
});

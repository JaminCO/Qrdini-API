document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm');
    const responseDiv = document.getElementById('response');

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the form from submitting the traditional way

        const inputData = document.getElementById('inputData').value;

        // Define your API URL
        const apiUrl = 'https://qrc-gen-api.onrender.com/generate'; // Replace with your actual API URL

        // Use the fetch API to send a POST request to the API
        fetch(apiUrl, {
            method: 'POST',
            body: JSON.stringify({ data: inputData }), // Convert data to JSON format if needed
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            // Display the API response in the responseDiv
            responseDiv.innerHTML = `<p>API Response: ${data.success}</p>`; // Modify this to match your API response structure
        })
        .catch(error => {
            console.error('Error:', error);
            responseDiv.innerHTML = '<p>Error occurred while fetching data from the API.</p>';
        });
    });
});

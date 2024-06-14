document.getElementById('pdf-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);

    document.getElementById('status').classList.remove('hidden');
    document.getElementById('result').classList.add('hidden');

    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').classList.add('hidden');
        if (data.success) {
            document.getElementById('estimated-time').textContent = data.processing_time;
            document.getElementById('found-password').textContent = data.password;
            document.getElementById('result').classList.remove('hidden');
            document.getElementById('download-link').href = data.download_url;
        } else {
            alert('Failed to decrypt the PDF. Exhausted all attempts.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('matchForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Submit form via fetch to keep the form on the same page
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                // Redirect to the next page after successful form submission
                window.location.href = "/generate/cricket/match_report/match-overview";
            } else {
                alert('There was an error submitting the form. Please try again.');
            }
        }).catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
});
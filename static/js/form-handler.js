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
                if (window.location.href == "/generate/cricket/match_report/main-details") {
                    window.location.href = "/generate/cricket/match_report/match-overview";
                }
                else if (window.location.href == "/generate/cricket/match_report/match-overview") {
                    window.location.href = "/generate/cricket/match_report/skill-breakdown";
                }
                else if (window.location.href == "/generate/cricket/match_report/skill-breakdown") {
                    window.location.href = "/generate/cricket/match_report/stats";
                }
                else if (window.location.href == "/generate/cricket/match_report/stats") {
                    window.location.href = "/generate/cricket/match_report/mentions";
                }
                else if (window.location.href == "/generate/cricket/match_report/mentions") {
                    window.location.href = "/generate/cricket/match_report/signoff";
                }
                else if (window.location.href == "/generate/cricket/match_report/signoff") {
                    window.location.href = "/generate/cricket/output/report";
                }
                else if (window.location.href == "/generate/cricket/session_planner") {
                    window.location.href = "/output/session_planner";
                }
            } else {
                alert('There was an error submitting the form. Please try again.');
            }
        }).catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
});
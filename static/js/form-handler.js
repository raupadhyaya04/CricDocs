document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('matchForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Log current action URL and pathname for debugging
        console.log("Form action URL:", form.action);
        console.log("Current pathname:", window.location.pathname);

        const formData = new FormData(form);

        // Send form data using fetch
        fetch(form.action, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                // Log successful submission
                console.log("Form submission successful. Redirecting...");

                // Get the current pathname
                const currentPath = window.location.pathname;

                // Log current path before redirecting
                console.log("Checking path for redirection:", currentPath);

                // Redirect based on current pathname
                switch (currentPath) {
                    case "/generate/cricket/match_report/main-details":
                        window.location.href = "/generate/cricket/match_report/match-overview";
                        break;
                    case "/generate/cricket/match_report/match-overview":
                        window.location.href = "/generate/cricket/match_report/skill-breakdown";
                        break;
                    case "/generate/cricket/match_report/skill-breakdown":
                        window.location.href = "/generate/cricket/match_report/stats";
                        break;
                    case "/generate/cricket/match_report/stats":
                        window.location.href = "/generate/cricket/match_report/mentions";
                        break;
                    case "/generate/cricket/match_report/mentions":
                        window.location.href = "/generate/cricket/match_report/signoff";
                        break;
                    case "/generate/cricket/match_report/signoff":
                        window.location.href = "/generate/cricket/output/report";
                        break;
                    case "/generate/cricket/session_planner":
                        window.location.href = "/output/session_planner";
                        break;
                    default:
                        console.log("No matching path for redirection.");
                }
            } else {
                console.error('Form submission failed. Status:', response.status);
                alert('There was an error submitting the form. Please try again.');
            }
        }).catch(error => {
            console.error('Fetch error:', error);
            alert('An error occurred. Please try again.');
        });
    });
});

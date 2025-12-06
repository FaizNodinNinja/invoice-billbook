document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('industry-form');
    if (!form) return;

    const industryNameInput = document.getElementById('industry-name');
    const industryDropdown = document.getElementById('industry');
    const industryModal = document.getElementById('industryModal');
    const toastEl = document.getElementById('successToast');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get CSRF token from cookie if input not found
        const getCookie = (name) => {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                document.cookie.split(';').forEach(cookie => {
                    const c = cookie.trim();
                    if (c.startsWith(name + '=')) cookieValue = decodeURIComponent(c.split('=')[1]);
                });
            }
            return cookieValue;
        }
        const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')?.value || getCookie('csrftoken');

        fetch('/ajax/add-industry/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: new URLSearchParams({ industry: industryNameInput.value })
        })
        .then(res => res.json())
        .then(data => {
            if (!data.id || !data.name) return alert("Something went wrong!");

            // Add option
            if (industryDropdown) {
                const newOption = new Option(data.name, data.id, true, true);
                industryDropdown.appendChild(newOption);
            }

            // Close modal safely
            if (industryModal) {
                industryModal.classList.remove('show');
                industryModal.style.display = 'none';
            }
            document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
            document.body.classList.remove('modal-open');

            // Show toast safely
            if (toastEl) {
                const toast = new bootstrap.Toast(toastEl, { delay: 1100 });
                toast.show();
            }

            if (industryNameInput) industryNameInput.value = '';
        })
        .catch(err => alert("Error: " + err.message));
    });
});


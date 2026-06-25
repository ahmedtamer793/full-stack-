document.addEventListener("DOMContentLoaded", () => {
    const cryForm = document.getElementById('cry-form');
    if (cryForm) {
        cryForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const output = document.getElementById('cry-output');
            const payload = {
                username: document.getElementById('username').value,
                css_property: document.getElementById('css-prop').value,
                story: document.getElementById('story').value
            };

            output.innerText = "Sending POST request to Flask...";
            try {
                const res = await fetch('/api/cry-room/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                if(res.ok) {
                    output.innerHTML = `<span style="color:yellow">Success! Database ID: ${data.complaint.id}</span><br>Story logged. Watch the live console!`;
                } else {
                    output.innerHTML = `<span style="color:red">Error: ${data.error}</span>`;
                }
            } catch (err) {
                output.innerText = "Server connection failed.";
            }
        });
    }
});
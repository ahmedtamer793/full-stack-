document.addEventListener("DOMContentLoaded", () => {
    const sqlForm = document.getElementById('sql-form');
    if (sqlForm) {
        sqlForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const output = document.getElementById('sql-output');
            const queryInput = document.getElementById('bad-query').value;

            output.innerText = "Analyzing execution plan...";
            try {
                const res = await fetch('/api/graveyard/autopsy', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: queryInput })
                });
                const data = await res.json();
                if (res.ok) {
                    output.innerHTML = `<strong>Sarcasm Engine:</strong> ${data.sarcasm}<br><br><strong>SQLite EXPLAIN QUERY PLAN:</strong><br>${data.plan}`;
                } else {
                    output.innerHTML = `<span style="color:red">Error: ${data.error}</span>`;
                }
            } catch (err) {
                output.innerText = "Analysis failed.";
            }
        });
    }

    const apiForm = document.getElementById('api-form');
    if (apiForm) {
        apiForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const output = document.getElementById('api-output');
            const payload = {
                url: document.getElementById('api-url').value,
                method: document.getElementById('api-method').value
            };

            output.innerText = "Flask is making the request...";
            try {
                const res = await fetch('/api/tester/run', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                if (res.ok) {
                    output.innerHTML = `Status Code: <strong>${data.status}</strong><br>Response Time: ${data.time_ms}ms<br>Comment: ${data.comment || 'Done.'}`;
                } else {
                    output.innerHTML = `<span style="color:red">Error: ${data.error}</span>`;
                }
            } catch (err) {
                output.innerText = "Request failed.";
            }
        });
    }
});
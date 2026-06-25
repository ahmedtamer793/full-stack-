document.addEventListener("DOMContentLoaded", () => {
    const consoleEl = document.getElementById('live-console');
    if (consoleEl) {
        const eventSource = new EventSource('/stream/logs');
        
        eventSource.onmessage = function(event) {
            const newLog = document.createElement('div');
            newLog.innerText = event.data;
            consoleEl.appendChild(newLog);
            consoleEl.scrollTop = consoleEl.scrollHeight;
        };
        
        eventSource.onerror = function(err) {
            console.error("SSE Failed:", err);
        };
    }

    const runawayBtn = document.getElementById('the-div');
    const container = document.getElementById('runaway-container');
    if (runawayBtn && container) {
        runawayBtn.addEventListener('mouseover', () => {
            const maxX = container.clientWidth - runawayBtn.clientWidth;
            const maxY = container.clientHeight - runawayBtn.clientHeight;
            runawayBtn.style.left = Math.floor(Math.random() * maxX) + 'px';
            runawayBtn.style.top = Math.floor(Math.random() * maxY) + 'px';
            runawayBtn.innerText = "Nice Try 😂";
        });
    }
});
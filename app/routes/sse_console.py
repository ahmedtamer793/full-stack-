from flask import Blueprint, Response
from app.utils.logger import log_queue
import time

sse_bp = Blueprint('sse', __name__)

@sse_bp.route('/logs')
def stream_logs():
    def generate():
        yield "data: [SYSTEM] Connected to Backend Mainframe SSE.\n\n"
        
        while True:
            if not log_queue.empty():
                msg = log_queue.get()
                yield f"data: {msg}\n\n"
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')
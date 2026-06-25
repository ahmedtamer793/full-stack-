from queue import Queue

log_queue = Queue(maxsize=100)

def push_log_event(action, status, details=""):
    """Format: [ACTION] STATUS - DETAILS"""
    message = f"[{action}] {status} - {details}"
    if log_queue.full():
        log_queue.get() # Remove oldest if full
    log_queue.put(message)
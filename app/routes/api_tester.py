from flask import Blueprint, request, jsonify
import requests
import time
from app.utils.logger import push_log_event

api_tester_bp = Blueprint('api_tester', __name__)

@api_tester_bp.route('/run', methods=['POST'])
def run_test():
    data = request.get_json() or {}
    target_url = data.get('url')
    method = data.get('method', 'GET').upper()

    if not target_url:
        return jsonify({'error': 'Missing URL'}), 400

    start_time = time.time()
    try:
        if method == 'GET':
            response = requests.get(target_url, timeout=5)
        elif method == 'POST':
            response = requests.post(target_url, timeout=5, json=data.get('body', {}))
        else:
            return jsonify({'error': 'Method not supported'}), 400
        
        response_time = int((time.time() - start_time) * 1000)
        
        push_log_event("API_TESTER", f"{response.status_code}", f"Tested {target_url} in {response_time}ms")
        
        return jsonify({
            'status': response.status_code,
            'time_ms': response_time,
            'headers_count': len(response.headers),
        }), 200

    except requests.exceptions.RequestException as e:
        push_log_event("API_TESTER", "ERROR", f"Failed to reach {target_url}")
        return jsonify({'status': 'Error', 'comment': str(e)}), 200
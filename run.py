import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    print("[SYSTEM] Anti-Frontend Server running on port 5000")
    print("[SYSTEM] No CSS allowed beyond this point.")
    app.run(debug=True, threaded=True)
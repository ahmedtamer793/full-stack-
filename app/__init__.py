from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes.home import home_bp
    from app.routes.cry_room import cry_room_bp
    from app.routes.api_tester import api_tester_bp
    from app.routes.graveyard import graveyard_bp
    from app.routes.sse_console import sse_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(cry_room_bp, url_prefix='/api/cry-room')
    app.register_blueprint(api_tester_bp, url_prefix='/api/tester')
    app.register_blueprint(graveyard_bp, url_prefix='/api/graveyard')
    app.register_blueprint(sse_bp, url_prefix='/stream')

    return app
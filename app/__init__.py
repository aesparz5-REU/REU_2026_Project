from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.student import student_bp
    from .routes.admin import admin_bp

    app.register_blueprint(student_bp)
    app.register_blueprint(admin_bp)

    return app

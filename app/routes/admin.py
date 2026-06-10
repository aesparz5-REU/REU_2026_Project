from flask import Blueprint, jsonify
from app.models import Scenario
from app.extensions import db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/scenarios")
def list_scenarios():
    scenarios = Scenario.query.all()
    return jsonify([
        {
            "key": s.key,
            "title": s.title,
            "objective": s.objective,
            "is_active": s.is_active
        } for s in scenarios
    ])

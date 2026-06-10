from flask import Blueprint, render_template, request, jsonify
from app.extensions import db
from app.models import SessionAttempt
from app.services.scenarios_runner import get_scenario
from app.services.logging_service import log_event

student_bp = Blueprint("student", __name__)

@student_bp.route("/")
def index():
    return render_template("index.html")

@student_bp.route("/scenario/<scenario_key>/start", methods = ["POST"])
def start_scenario(scenario_key):
    scenario = get_scenario(scenario_key)
    if not scenario:
        return jsonify({"error": "Scenario not found"}), 404
    
    attempt = SessionAttempt(scenario_key = scenario_key, state = "not_started")
    db.session.add(attempt)
    db.session.commit()

    payload = scenario.start(attempt)
    db.session.commit()

    log_event(attempt.id, "scenario.started", {"scenario_key": scenario_key})
    return jsonify({"attempt_id": attempt.id, "payload": payload})

@student_bp.route("/scenario/<int:attempt_id>/action", methods = ["POST"])
def scenario_action(attempt_id):
    attempt = SessionAttempt.query.get_or_404(attempt_id)
    scenario = get_scenario(attempt.scenario_key)
    if not scenario:
        return jsonify({"error": "Scenario not found"}), 404
    
    data = request.get_json(silent = True) or {}
    action = data.get("action")
    
    result = scenario.handle_action(attempt, action, data)
    db.session.commit()

    log_event(attempt.id, "action", {"action": action, "data": data, "result": result})
    return jsonify(result)

@student_bp.route("/scenario/<int:attempt_id>/debrief")
def scenario_debrief(attempt_id):
    attempt = SessionAttempt.query.get_or_404(attempt_id)
    scenario = get_scenario(attempt.scenario_key)
    if not scenario:
        return jsonify({"error": "Scenario not found"}), 404
    
    payload = scenario.debrief(attempt)
    return render_template("debrief.html", payload = payload)

@student_bp.route("/scenario/<int:attempt_id>/reset", methods = ["POST"])
def reset_scenario(attempt_id):
    attempt = SessionAttempt.query.get_or_404(attempt_id)
    attempt.state = "not_started"
    attempt.score = 0
    db.session.commit()
    return jsonify({"ok": True, "message": "Scenario reset"})


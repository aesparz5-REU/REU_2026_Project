from datetime import datetime
from .extensions import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    objective = db.Column(db.Text, nullable=False)
    debrief = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class SessionAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scenario_key = db.Column(db.String(100), nullable=False)
    student_name = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, default = 0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class EventLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('session_attempt.id'), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    payload = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

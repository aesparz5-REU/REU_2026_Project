import json
from app.extensions import db
from app.models import EventLog

def log_event(attempt_id, event_type, payload = None):
    entry = EventLog(
        attempt_id = attempt_id,
        event_type = event_type,
        payload = json.dumps(payload or {})
    )
    db.session.add(entry)
    db.session.commit()

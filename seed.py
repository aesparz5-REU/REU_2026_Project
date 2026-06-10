from app import create_app
from app.extensions import db
from app.models import Scenario

app = create_app()

with app.app_context():
    if not Scenario.query.filter_by(key="telemetry_tampering").first():
        db.session.add(
            Scenario(
                key="telemetry_tampering",
                title="Telemetry Integrity Investigation",
                objective="Identify signs of manipulated telemetry in a mock monitoring environment.",
                debrief="Focus on integrity checks, anomaly detection, and source validation.",
            )
        )
        db.session.commit()
        print("Seeded telemetry_tampering scenario.")
    else:
        print("Scenario already exists.")
from .base import Scenario

class TelemetryTamperScenario(Scenario):
    key = "telemetry_tamper"
    title = "Telemetry Integrity Investigation"

    def start(self, attempt):
        attempt.state = "initialized"
        return {
            "title": self.title,
            "objective": (
                "Investigate a suspected telemetry manipulation even and "
                "idnetify signs of data tampering."
            ),
            "message": "A monitoring system reports suspiciously high production values.",
            "checkpoint": "Review the evidence and decide whether the data is trustworthy."
        }
    
    def handle_action(self, attempt, action, data = None):
        if attempt.state == "initialized" and action == "inspect-dashboard":
            attempt.state = "dashboard_reviewed"
            return {
                "ok": True,
                "message": "You reviewed the dashboard and found unusual values."
            }

        if attempt.state == "dashboard_reviewed" and action == "answer_quiz":
            answer = (data or {}).get("answer", "").strip().lower()
            if answer in {"yes", "y", "tampered", "manipulated"}:
                attempt.state = "complete"
                attempt.score = 100
                return {
                    "ok": True,
                    "message": "Correct! The evidence is consistent with data tampering."
                }
            else:
                attempt.score = 50
                return {
                    "ok": False,
                    "message": "Not quite. Re-examine the indicators of integrity loss."
                }
            
        return {
            "ok": False,
            "message": "Action not recognized or not valid in the current state."
        }
    
    def debrief(self, attempt):
        return {
            "scenario": self.title,
            "score": attempt.score,
            "state": attempt.state,
            "debrief": (
                "The exercise demonstrated how falsified telemetry can mislead operators."
                "Students should look for inconsistencies, unexpected value jumps and"
                "mismatches between source and reported output."
            )
        }
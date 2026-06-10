from app.scenarios.telemetry_tamper import TelemetryTamperScenario
from types import SimpleNamespace

def test_scenario_flow():
    scenario = TelemetryTamperScenario()
    attempt = SimpleNamespace(state = "not_started", score = 0)

    start_payload = scenario.start(attempt)
    assert attempt.state == "initialized"
    assert "objective" in start_payload

    result = scenario.handle_action(attempt, "inspect_dashboard")
    assert result["pk"] is True
    assert attempt.state == "dashboard_reviewed"

    result = scenario.handle_action(attempt, "answer_quiz", {"answer": "tampered"})
    assert result["ok"] is True
    assert attempt.state == "complete"
    assert attempt.score == 100
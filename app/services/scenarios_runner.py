from app.scenarios.telemetry_tamper import TelemetryTamperScenario

SCENARIOS = {
    TelemetryTamperScenario.key: TelemetryTamperScenario(),
}

def get_scenario(key):
    return SCENARIOS.get(key)
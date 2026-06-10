class Scenario:
    key = "base"
    title = "Base Scenario"

    def start(self, attempt):
        raise NotImplementedError
    
    def handle_action(self, attempt, action, data = None):
        raise NotImplementedError
    
    def debrief(self, attempt):
        raise NotImplementedError
    
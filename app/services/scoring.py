def score_action(current_score, action_result):
    if action_result.get("ok"):
        return min(100, current_score + 50)
    return current_score

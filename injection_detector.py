# Simple prompt injection detector

suspicious_patterns = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass safety",
    "developer mode",
    "act as unrestricted",
]

def detect_injection(text):

    score = 0

    for pattern in suspicious_patterns:
        if pattern in text.lower():
            score += 1

    return score
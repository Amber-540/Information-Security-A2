from config import ALLOW, MASK, BLOCK, INJECTION_BLOCK_THRESHOLD

def policy_decision(injection_score, pii_results):

    if injection_score >= INJECTION_BLOCK_THRESHOLD:
        return BLOCK

    if len(pii_results) > 0:
        return MASK

    return ALLOW
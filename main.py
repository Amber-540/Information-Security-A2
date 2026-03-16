import time
from injection_detector import detect_injection
from presidio_scanner import detect_pii, mask_pii
from policy_engine import policy_decision


def process_input(user_input):

    start = time.time()

    injection_score = detect_injection(user_input)

    pii_results = detect_pii(user_input)

    decision = policy_decision(injection_score, pii_results)

    if decision == "BLOCK":
        output = "Request blocked due to security risk."

    elif decision == "MASK":
        output = mask_pii(user_input, pii_results)

    else:
        output = user_input

    end = time.time()

    latency = end - start

    print("Decision:", decision)
    print("Latency:", latency)

    return output


if __name__ == "__main__":

    text = input("Enter prompt: ")

    result = process_input(text)

    print("Output:", result)
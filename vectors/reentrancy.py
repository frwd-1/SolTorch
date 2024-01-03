import re

external_call_pattern = re.compile(r"\.(call|send|transfer)\(")
state_change_pattern = re.compile(r"^[ \t]*(\w+)[ \t]*=[ \t]*")


def detect_reentrancy(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    potential_vulnerabilities = []
    external_call_detected = False

    for i, line in enumerate(lines):
        if external_call_pattern.search(line):
            external_call_detected = True
        elif external_call_detected and state_change_pattern.search(line):
            potential_vulnerabilities.append((i + 1, line.strip()))

    return potential_vulnerabilities


# Assuming you have already trained your model 'model' and have a 'vectorizer'


def predict_reentrancy(code):
    features = vectorizer.transform([code])
    prediction = model.predict(features)
    return prediction[
        0
    ]  # returns 1 for potential vulnerability, 0 for no vulnerability

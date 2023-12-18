import os
import re


folder_path = "/path/to/solidity/contracts"


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


def main():
    for filename in os.listdir(folder_path):
        if filename.endswith(".sol"):
            file_path = os.path.join(folder_path, filename)
            vulnerabilities = detect_reentrancy(file_path)

            if vulnerabilities:
                print(f"Potential reentrancy vulnerabilities in {filename}:")
                for line_num, line in vulnerabilities:
                    print(f"  Line {line_num}: {line}")


if __name__ == "__main__":
    main()

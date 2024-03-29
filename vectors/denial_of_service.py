# can happen due to unbounded for loops or external call failure
# questions to ask: is the iterable bounded? is the external call guaranteed to succeed?
# if the call fails, the state changes are reverted, so no vulnerability
# see DOS https://www.youtube.com/watch?v=pUWmJ86X_do at 5:22:00
def detect_dos_vulnerabilities(code):
    # Split the code into lines
    lines = code.split("\n")

    # Initialize a list to store the vulnerable lines
    vulnerable_lines = []

    # Iterate over each line of code
    for i, line in enumerate(lines):
        # Check if the line contains a for loop
        if "for" in line:
            # Check if the for loop is unbounded
            if "uint" not in line and "int" not in line:
                vulnerable_lines.append(i + 1)  # Add the line number to the list

    return vulnerable_lines


# Example usage
solidity_code = """
contract MyContract {
    function foo() public {
        for (uint i = 0; ; i++) {
            // Unbounded for loop
        }
    }
}
"""

vulnerable_lines = detect_dos_vulnerabilities(solidity_code)
print("Vulnerable lines:", vulnerable_lines)

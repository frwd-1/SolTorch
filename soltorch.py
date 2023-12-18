import os
from vectors.reentrancy import detect_reentrancy

folder_path = "/path/to/solidity/contracts"


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

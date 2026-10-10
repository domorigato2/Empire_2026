import os
import sys

def search_files(keyword, target_dir="."):
    print("\n==================================================")
    print("      CLI UTILITY // RECURSIVE GREP SEARCH        ")
    print("==================================================")
    print(f" Keyword   : '{keyword}'")
    print(f" Directory : {os.path.abspath(target_dir)}")
    print("--------------------------------------------------")

    matches = 0
    for root, dirs, files in os.walk(target_dir):
        # Skip hidden git folders
        if ".git" in root:
            continue
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        if keyword.lower() in line.lower():
                            print(f" [+] {file} (Line {line_num}):")
                            print(f"     {line.strip()}")
                            print("-" * 50)
                            matches += 1
            except Exception:
                pass

    print(f" Search Complete. Total Matches Found: {matches}")
    print("==================================================\n")

if __name__ == "__main__":
    term = sys.argv[1] if len(sys.argv) > 1 else "def "
    search_files(term)

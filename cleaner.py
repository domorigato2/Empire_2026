import os
import shutil
import sys

EXTENSIONS = {
    "Python": [".py"],
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Config": [".json", ".yaml", ".ini", ".log"]
}

def organize_directory(target_dir="."):
    print("\n==================================================")
    print("      DIRECTORY ORGANIZER // AUTO-SORT ENGINE     ")
    print("==================================================")
    print(f" Target Path : {os.path.abspath(target_dir)}")
    print(" Scanning and sorting files by extension...")
    print("--------------------------------------------------")

    if not os.path.exists(target_dir):
        print(f"[!] Directory '{target_dir}' does not exist.")
        return

    moved_count = 0
    for filename in os.listdir(target_dir):
        if os.path.isdir(filename):
            continue
        
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        assigned_folder = "Misc"
        for category, exts in EXTENSIONS.items():
            if ext in exts:
                assigned_folder = category
                break

        folder_path = os.path.join(target_dir, assigned_folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        src = os.path.join(target_dir, filename)
        dst = os.path.join(folder_path, filename)
        
        # Never move the automation scripts themselves
        if filename.endswith(".py"):
            continue

        try:
            shutil.move(src, dst)
            print(f" [+] Sorted: {filename:<25} --> {assigned_folder}/")
            moved_count += 1
        except Exception as e:
            print(f" [-] Failed to move {filename}: {e}")

    print("--------------------------------------------------")
    print(f" Organization Complete. Total Files Sorted: {moved_count}")
    print("==================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_directory(target)

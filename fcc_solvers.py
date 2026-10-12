# Save as fcc_solvers.py in C:\Users\sheil\Empire_2026\

def caesar_cipher(text, shift):
    """FreeCodeCamp Vigenere/Caesar Cipher Module"""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def arithmetic_arranger(problems, show_answers=False):
    """FreeCodeCamp Project: Arithmetic Formatter"""
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line, second_line, dashes, answers = [], [], [], []
    
    for p in problems:
        parts = p.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
            
        width = max(len(parts[0]), len(parts[2])) + 2
        first_line.append(parts[0].rjust(width))
        second_line.append(parts[1] + " " + parts[2].rjust(width - 2))
        dashes.append("-" * width)
        
        ans = str(int(parts[0]) + int(parts[2])) if parts[1] == '+' else str(int(parts[0]) - int(parts[2]))
        answers.append(ans.rjust(width))

    arranged = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)
    if show_answers:
        arranged += "\n" + "    ".join(answers)
    return arranged

if __name__ == "__main__":
    print("\n" + "="*60)
    print(" FREECODECAMP PYTHON ALGORITHM ENGINE")
    print("="*60)
    
    # Cipher Test
    encrypted = caesar_cipher("ROOT KERNEL OPERATOR DOMINIC", 3)
    print(f" [+] Encrypted Cipher : {encrypted}")
    print(f" [+] Decrypted Cipher : {caesar_cipher(encrypted, -3)}")
    
    print("-" * 60)
    
    # Arithmetic Formatter Test
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(problems, show_answers=True))
    print("="*60 + "\n")
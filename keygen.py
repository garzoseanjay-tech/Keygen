import os
import random
import string
import hashlib

# Enable ANSI colors in Windows Command Prompt
os.system("")

SECRET_SALT = "TRISTAN_GCREATE_V1_PREMIUM"

class Colors:
    GREEN = '\033[92m'
    DARK_GREEN = '\033[32m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def generate_key():
    # Random mix of uppercase letters and numbers (4 chars)
    alphabet = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(alphabet, k=4))
    # Cryptographic signature that gcreate.py verifies
    sig = hashlib.sha256(f"{code}:{SECRET_SALT}".encode()).hexdigest()[:4].upper()
    return f"GCREATE-{code}-{sig}"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Colors.GREEN}{Colors.BOLD}")
    print("  ╔═════════════════════════════════════════════════════════╗")
    print("  ║        GCREATE v1.0 PREMIUM  |  PRIVATE KEYGEN          ║")
    print("  ╚═════════════════════════════════════════════════════════╝")
    print(f"{Colors.RESET}")

    while True:
        try:
            raw = input(f"{Colors.GREEN}  » How many random keys to generate? (default 5): {Colors.RESET}").strip()
            count = int(raw) if raw else 5
            if count < 1:
                raise ValueError
            break
        except ValueError:
            print(f"{Colors.RED}  [!] Enter a valid number (1 or higher).{Colors.RESET}")

    keys = [generate_key() for _ in range(count)]

    print(f"\n{Colors.DARK_GREEN}  ═══════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.YELLOW}{Colors.BOLD}  [ GENERATED ACCESS KEYS ]{Colors.RESET}")
    for i, k in enumerate(keys, 1):
        print(f"{Colors.DARK_GREEN}  [{i:02d}] » {Colors.GREEN}{Colors.BOLD}{k}{Colors.RESET}")
    print(f"{Colors.DARK_GREEN}  ═══════════════════════════════════════════════════════════{Colors.RESET}\n")

    save = input(f"{Colors.GREEN}  » Save these keys to generated_keys.txt? (y/n): {Colors.RESET}").strip().lower()
    if save == 'y':
        with open("generated_keys.txt", "a", encoding="utf-8") as f:
            f.write("=== GCREATE v1.0 PREMIUM KEYS ===\n")
            for k in keys:
                f.write(f"{k}\n")
            f.write("\n")
        print(f"{Colors.GREEN}{Colors.BOLD}  [✓] Saved {len(keys)} keys to {os.path.abspath('generated_keys.txt')}{Colors.RESET}")

if __name__ == "__main__":
    main()
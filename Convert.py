import re

with open("key_logs.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

message = ""
for line in lines:
    match = re.search(r'key pressed\s+"(.)"', line)
    if match:
        print(f"[Matched] {match.group(1)}")  # Debugging output
        message += match.group(1)
    else:
        print(f"[Skipped] {line.strip()}")  # Help us debug

print("🟢 Reconstructed Message:", message)

from pathlib import Path
import os
import sys
import json

if len(sys.argv) != 2:
    print("Usage: python3 process_audit.py <PID>")
    sys.exit(1)
try:
    pid = int(sys.argv[1])
except ValueError:
    print("Error: PID must be a number")
    sys.exit(1)
status_file = Path(f"/proc/{pid}/status")

try:
    status = status_file.read_text()
except (FileNotFoundError, PermissionError) as error:
    print(f"Cannot inspect process: {error}")
    sys.exit(1)

print(f"Investigating PID: {pid}")

for line in status.splitlines():
    if line.startswith(("Name:", "State:", "PPid:", "Uid:")):
        print(line)

print(f"Investigator UID: {os.getuid()}")
report = {
    "pid": pid,
    "investigator_uid": os.getuid()
}

for line in status.splitlines():
    if line.startswith(("Name:", "State:", "PPid:", "Uid:")):
        key, value = line.split(":", 1)
        report[key.lower()] = value.strip()

print(json.dumps(report, indent=4))

import subprocess

result = subprocess.run(
    ["python3", "process_audit.py", "-5"],
    capture_output=True,
    text=True
)

assert result.returncode == 1
assert "positive integer" in result.stdout

print("PASS: Negative PID correctly rejected")

import os
import json

pid = os.getpid()

result = subprocess.run(
    ["python3", "process_audit.py", str(pid)],
    capture_output=True,
    text=True
)

assert result.returncode == 0

report = json.loads(result.stdout)

assert report["pid"] == pid
assert report["investigator_uid"] == os.getuid()

print("PASS: Valid PID produces correct JSON")

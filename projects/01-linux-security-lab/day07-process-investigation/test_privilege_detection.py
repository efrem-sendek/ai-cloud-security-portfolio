from privilege_detection import detect_privilege_escalation

assert detect_privilege_escalation(1000, 1000) == False
print("PASS: Normal user process")

assert detect_privilege_escalation(0, 0) == False
print("PASS: Normal root process")

assert detect_privilege_escalation(1000, 0) == True
print("PASS: Potential privilege escalation detected")

assert detect_privilege_escalation(1001, 1001) == False
print("PASS: Non-root user process")

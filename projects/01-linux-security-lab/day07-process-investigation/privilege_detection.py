def detect_privilege_escalation(real_uid, effective_uid):
    return real_uid != 0 and effective_uid == 0


import json
import os

process = {
    "name": "python",
    "pid": os.getpid(),
    "uid": os.getuid()
}

print(json.dumps(process, indent=4))

import json
import os
from datetime import datetime

def kontrol_et():
    now = datetime.now().isoformat()
    return {
        "timestamp": now,
        "location": "Bayonne",
        "status": "not found",
        "message": "Test log - Render'dan çalıştı!"
    }

def log_yaz(data):
    log_file = os.path.join(os.path.dirname(__file__), "log.json")

    if not os.path.exists(log_file):
        logs = []
    else:
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(data)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=2)

if __name__ == "__main__":
    print("Render bot başladı")
    sonuc = kontrol_et()
    log_yaz(sonuc)
    print("Render log yazıldı")

import json
import os
from datetime import datetime

def kontrol_et():
    now = datetime.now().isoformat()
    return {
        "timestamp": now,
        "location": "Bayonne",
        "status": "not found",
        "message": "Test log - everything works"
    }

def log_yaz(data):
    log_file = "log.json"

    # GitHub Actions içinde bulunduğu path'e yazma hatasını önle
    full_path = os.path.join(os.path.dirname(__file__), log_file)

    if not os.path.exists(full_path):
        logs = []
    else:
        try:
            with open(full_path, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(data)

    with open(full_path, "w") as f:
        json.dump(logs, f, indent=2)

if __name__ == "__main__":
    print("Bot başladı")
    sonuc = kontrol_et()
    log_yaz(sonuc)
    print("Log yazıldı")


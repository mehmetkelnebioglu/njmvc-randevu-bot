import json
from datetime import datetime

def kontrol_et():
    now = datetime.now().isoformat()
    # Örnek dummy veri
    return {
        "timestamp": now,
        "location": "Bayonne",
        "status": "not found",
        "message": "Bu sadece test verisidir."
    }

def log_yaz(data):
    try:
        with open("log.json", "r") as f:
            logs = json.load(f)
    except Exception:
        logs = []
    
    logs.append(data)
    
    with open("log.json", "w") as f:
        json.dump(logs, f, indent=2)

if __name__ == "__main__":
    print("Bot çalışıyor...")  # loglarda görmek için
    sonuc = kontrol_et()
    log_yaz(sonuc)

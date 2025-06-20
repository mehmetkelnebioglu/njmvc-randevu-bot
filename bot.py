import json
from datetime import datetime

# Bu kısmı NJMVC kontrol koduyla sonra değiştireceğiz
def kontrol_et():
    return {
        "timestamp": datetime.now().isoformat(),
        "location": "Bayonne",
        "status": "not found",
        "message": "Uygun randevu yok"
    }

def log_yaz(data):
    try:
        with open("log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []
    logs.append(data)
    with open("log.json", "w") as f:
        json.dump(logs, f, indent=2)

if __name__ == "__main__":
    sonuc = kontrol_et()
    log_yaz(sonuc)

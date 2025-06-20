import json
import datetime

log_data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "location": "Bayonne",
    "status": "not found",
    "message": "Test log - Render'dan çalıştı!"
}

# JSON dosyasına yaz
with open("log.json", "w") as f:
    json.dump(log_data, f)

# Konsola da yazdır
print("==== Bot Log ====")
print(json.dumps(log_data, indent=2))


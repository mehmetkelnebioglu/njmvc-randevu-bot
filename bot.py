import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import json
import datetime

# Ayarlar
target_locations = ["Bayonne", "Elizabeth", "Edison", "Lodi", "Freehold", "Newark", "North Bergen", "Paterson", "Wayne"]
start_date = "06/20/2025"
end_date = "07/05/2025"

def check_appointment():
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = uc.Chrome(options=options)
    driver.get("https://telegov.njportal.com/njmvc/AppointmentWizard/15")  # örnek URL

    time.sleep(3)

    results = []

    for loc in target_locations:
        try:
            # Lokasyon seçimi
            location_element = driver.find_element(By.XPATH, f"//div[contains(text(), '{loc}')]")
            location_element.click()
            time.sleep(2)

            # Tarih kontrolü (sayfada uygun tarih var mı?)
            page_source = driver.page_source
            if start_date in page_source or end_date in page_source:
                results.append({"location": loc, "available": True})
            else:
                results.append({"location": loc, "available": False})

            driver.back()
            time.sleep(2)
        except Exception as e:
            results.append({"location": loc, "error": str(e)})

    driver.quit()
    return results

# Çalıştır
output = check_appointment()

# Log kaydı
log = {
    "timestamp": datetime.datetime.now().isoformat(),
    "results": output
}

with open("log.json", "w") as f:
    json.dump(log, f, indent=2)

print("==== Randevu Kontrol Logu ====")
print(json.dumps(log, indent=2))

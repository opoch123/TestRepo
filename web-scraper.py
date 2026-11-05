from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

all_tables = []

for i in range(1, 11):
    url = f"https://charts.theglobeandmail.com/YluNf/{i}/"
    driver.get(url)
    time.sleep(5)

    tables = pd.read_html(driver.page_source)
    
    if tables:
        all_tables.append(tables[0])
        print(f"Page {i} scraped")
    else:
        print(f"No table found on page {i}")

driver.quit()

combined = pd.concat(all_tables, ignore_index=True)
combined.to_excel("DividendAllStars.xlsx", index=False)

print("DONE — file saved as DividendAllStars.xlsx")
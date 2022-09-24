import time

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

supportID = input("Input support ID: ")
loginCookie = input("Input pterodactyl_session cookie: ")
refreshRate = int(input("Input rerfesh time in seconds: "))
chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = uc.Chrome(use_subprocess=True,options=chrome_options,service_log_path='NUL')
driver.get("https://dash.icehost.pl/")
driver.add_cookie({"name":"pterodactyl_session","value":str(loginCookie)})
time.sleep(2)
driver.get("https://dash.icehost.pl/server/"+str(supportID))
while True:
    driver.save_screenshot("screen.png")
    refreshButton = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/section/div[1]/div[1]/div[2]/div[2]/div/button[1]"))
    )
    refreshButton.click()
    print("Server refreshed succesfully!")
    time.sleep(refreshRate)
input("")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def book_bobst_room(username, password, booking_time):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium"  # Required on Render

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Open Bobst room booking page
        driver.get("https://library.nyu.edu/spaces/bobst-group-study-rooms/")
        time.sleep(3)

        # Step 2: Click "Reserve a Room"
        reserve_btn = driver.find_element(By.LINK_TEXT, "Reserve a Room")
        reserve_btn.click()
        time.sleep(5)

        # Step 3: Log in with NetID
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(5)

        # Step 4: Simulate a booking step (this is where actual booking UI logic goes)
        return {"status": "success", "message": f"Simulated booking for {booking_time}"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        driver.quit()

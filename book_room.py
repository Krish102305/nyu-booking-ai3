from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def book_bobst_room(username, password, booking_time):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = "/usr/bin/chromium"

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 1. Go to NYU Library room page
        driver.get("https://library.nyu.edu/spaces/bobst-group-study-rooms/")
        time.sleep(2)

        # 2. Wait and click "Reserve a room"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Reserve a room"))
        )
        driver.find_element(By.LINK_TEXT, "Reserve a room").click()
        time.sleep(2)

        # 3. Switch to new tab or window
        driver.switch_to.window(driver.window_handles[-1])

        # 4. Click "Login"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        driver.find_element(By.LINK_TEXT, "Login").click()

        # 5. NYU Login form
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

        # 6. Wait for booking slot to load and click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{booking_time}')]"))
        )
        driver.find_element(By.XPATH, f"//button[contains(text(), '{booking_time}')]").click()

        # 7. Confirm
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-submit"))
        )
        driver.find_element(By.ID, "btn-submit").click()

        return {"status": "success", "time": booking_time}

    except Exception as e:
        driver.save_screenshot("error_debug.png")  # Optional: debug visual
        return {"status": "error", "message": str(e)}

    finally:
        driver.quit()

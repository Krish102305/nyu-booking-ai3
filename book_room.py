from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time as t

def book_bobst_room(username, password, booking_time):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = "/usr/bin/chromium"
    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://library.nyu.edu/spaces/bobst-group-study-rooms/")
        t.sleep(3)

        # Click "Reserve a Room"
        reserve_button = driver.find_element(By.LINK_TEXT, "Reserve a Room")
        reserve_button.click()
        t.sleep(5)

        # NYU Login
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()
        t.sleep(5)

        # NOTE: You’ll need to add steps here to select time, confirm details, etc.
        # For now we simulate success:
        return {"status": "success", "message": f"Simulated booking for {booking_time}"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        driver.quit()
    }
def book_bobst_room(username, password, booking_time):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Open Bobst room booking page
        driver.get("https://library.nyu.edu/spaces/bobst-group-study-rooms/")
        time.sleep(2)

        # Step 2: Click "Reserve a room"
        reserve_btn = driver.find_element(By.LINK_TEXT, "Reserve a room")
        reserve_btn.click()

        # Step 3: Switch to new tab and wait for login
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        driver.find_element(By.LINK_TEXT, "Login").click()

        # Step 4: Log in with NetID
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

        # Step 5: Wait for booking time and click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{booking_time}')]"))
        )
        driver.find_element(By.XPATH, f"//button[contains(text(), '{booking_time}')]").click()

        # Step 6: Confirm the booking
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
        driver.find_element(By.ID, "btn-submit").click()

        return {"status": "success", "time": booking_time}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        driver.quit()

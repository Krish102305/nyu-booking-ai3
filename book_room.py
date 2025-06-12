{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww29200\viewh15960\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from selenium import webdriver\
from selenium.webdriver.common.by import By\
from selenium.webdriver.chrome.options import Options\
import time\
\
def book_bobst_room(username, password, booking_time):\
    options = Options()\
    options.add_argument("--headless")\
    options.add_argument("--no-sandbox")\
    options.add_argument("--disable-dev-shm-usage")\
    driver = webdriver.Chrome(options=options)\
\
    try:\
        driver.get("https://library.nyu.edu/spaces/bobst-group-study-rooms/")\
        time.sleep(2)\
\
        # Login simulation \'97 adjust this based on actual HTML (requires inspection)\
        try:\
            driver.find_element(By.ID, "username").send_keys(username)\
            driver.find_element(By.ID, "password").send_keys(password)\
            driver.find_element(By.NAME, "submit").click()\
            time.sleep(3)\
        except:\
            print("Login fields not found or handled via NYU SSO")\
\
        # Navigate booking page and try booking \'97 placeholder only\
        return \{\
            "status": "success",\
            "message": f"Simulated login. Booking at \{booking_time\} would be attempted here."\
        \}\
\
    except Exception as e:\
        return \{"status": "error", "message": str(e)\}\
    finally:\
        driver.quit()}
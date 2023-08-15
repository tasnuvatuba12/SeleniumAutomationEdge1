import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def upload_file():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/upload")

    try:
        choose_file_button = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#file-upload")))

        choose_file_button.send_keys("C:\\Users\\Asus\\Downloads\\image11.png")

        upload_button = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#file-submit")))

        upload_button.click()

        time.sleep(3)
    except Exception as e:
        print("Upload page Exception: ", type(e).__name__)


upload_file()
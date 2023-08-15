"""
1. Wait for a specified amount of time for an element to appear
    for specified condition to be meet
    before throwing an exception(NoSuchElementException) and
    allow pooling frequency for wait.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_valid():
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        # Step 3: Find Username
        username = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username2']")))
        # Step 4: Enter Username
        username.send_keys("Admin")

    except Exception as e:
        print("Username Field Exception:", type(e).__name__)

    try:
        # Step 5: Find Password
        password = WebDriverWait(driver, 10, poll_frequency=4).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
        # Step 6: Enter Password
        password.send_keys("admin123")
    except Exception as e:
        print("password Field Exception:", type(e).__name__)

    # Step 7: Find Login Button
    try:
        login_button = WebDriverWait(driver, 15, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
        # Step 8: Click Login Button
        login_button.click()
    except Exception as e:
        print("Login button Exception:", type(e).__name__)


test_login_valid()

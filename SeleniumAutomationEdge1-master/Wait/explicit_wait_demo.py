"""
1. Wait for a specified amount of time for an element to appear
    for specified condition to be meet
    before throwing an exception(NoSuchElementException).
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

    explicit_wait = WebDriverWait(driver, 10)

    # Step 3: Find Username
    username = explicit_wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

    # Step 4: Find Password
    password = explicit_wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

    # Step 5: Fine Login Button
    login_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))

    # Step 6: Enter Username
    username.send_keys("Admin")

    # Step 7: Enter Password
    password.send_keys("admin123")

    # Step 8: Click Login Button
    login_button.click()


test_login_valid()

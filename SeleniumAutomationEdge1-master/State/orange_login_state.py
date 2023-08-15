from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(username, password):
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        # Step 3: Find Username
        username_field = WebDriverWait(driver, 10, poll_frequency=3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

        # Verify Username field is Enabled
        try:
            # Verify Username field is Enabled
            assert username_field.is_enabled(), f"Password field Disabled."
            # Step 6: Enter Password
            username_field.send_keys(username)
            print("Username field Enabled.Enter Password")
        except Exception as e:
            print("Username field error")

    except Exception as e:
        print("Username Field Exception:", type(e).__name__)

    try:
        # Step 5: Find Password
        password_field = WebDriverWait(driver, 10, poll_frequency=4).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

        try:
            # Verify Username field is Enabled
            assert password_field.is_enabled(), f"Password field Disabled."
            # Step 6: Enter Password
            password_field.send_keys(password)
            print("Password field Enabled.Enter Password")
        except Exception as e:
            print("Password field error")

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


test_login("Admin", "admin123")

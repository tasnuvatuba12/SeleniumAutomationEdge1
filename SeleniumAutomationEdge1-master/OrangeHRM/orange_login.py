from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_valid():
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 3: Find Username
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    # Step 4: Find Password
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    # Step 5: Fine Login Button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

    # Step 6: Enter Username
    username.send_keys("Admin")

    # Step 7: Enter Password
    password.send_keys("admin123")

    # Step 8: Click Login Button
    login_button.click()


def test_login_invalid():
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 3: Find Username
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    # Step 4: Find Password
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    # Step 5: Fine Login Button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

    # Step 6: Enter Username
    username.send_keys("Admin123")

    # Step 7: Enter Password
    password.send_keys("admin123")

    # Step 8: Click Login Button
    login_button.click()


test_login_valid()
test_login_invalid()

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


def test_add_to_cart(username, password):
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://www.saucedemo.com/")

    try:
        # Verify login page by Title
        assert "Swag Labs" in driver.title, f"Its not Login page.Title Mismatched."
        print("Login page Open Successfully.")

        try:
            # Step 3: Find Username
            username_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
            # Step 4: Enter Username
            username_field.send_keys(username)

        except Exception as e:
            print("Username Field Exception:", type(e).__name__)

        try:
            # Step 5: Find Password
            password_field = WebDriverWait(driver, 10, poll_frequency=4).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
            # Step 6: Enter Password
            password_field.send_keys(password)
        except Exception as e:
            print("password Field Exception:", type(e).__name__)

        # Step 7: Find Login Button
        try:
            login_button = WebDriverWait(driver, 15, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='login-button']")))
            # Step 8: Click Login Button
            login_button.click()
        except Exception as e:
            print("Login button Exception:", type(e).__name__)

        # Verify login or not
        assert "https://www.saucedemo.com/inventory.html" in driver.current_url, f"Login failed."
        print("Login successful.")

        # Add to Cart
        try:
            add_to_cart_button = WebDriverWait(driver, 15, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='add-to-cart-sauce-labs-backpack']")))
            # Step 8: Click Login Button
            add_to_cart_button.click()
        except Exception as e:
            print("Login button Exception:", type(e).__name__)

        # Shopping cart
        try:
            shopping_cart_button = WebDriverWait(driver, 15, poll_frequency=2).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link")))
            # Step 8: Click Login Button
            shopping_cart_button.click()
            print("Item Clicked")
        except Exception as e:
            print("Shopping cart button Exception:", type(e).__name__)

            # Verify cart page open or not
        assert "https://www.saucedemo.com/cart.html" in driver.current_url, f"Cart page failed."
        print("Cart page open successful.")

    except Exception as e:
        print("Login page Exception:", type(e).__name__)


test_add_to_cart("standard_user", "secret_sauce")

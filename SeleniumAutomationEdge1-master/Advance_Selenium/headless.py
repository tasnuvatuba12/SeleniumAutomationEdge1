import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Fund_Transfer.common import write_file
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_fund_transfer(account_type, transfer_type, amount, expected_amount):
    # Step 1: Browser Launch
    options = ChromeOptions()
    options.add_argument("-headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("http://127.0.0.1:5000/")

    try:
        # Verify home page by Title
        assert "Fund Transfer" in driver.title, f"Its not Login page.Title Mismatched."
        # print("Fund Transfer Open Successfully.")
        write_file("./fund_transfer_test.txt", "Fund Transfer Open Successfully.")

        try:
            # Step 3: Find Account
            account_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#account_type")))
            # Step 4: Select Account
            account_options = Select(account_field)
            if account_type == "savings":
                account_options.select_by_value("savings")
                # print(f"{account_type} Select Successfully.")
                write_file("./fund_transfer_test.txt", f"{account_type} Select Successfully.")
            if account_type == "current":
                account_options.select_by_value("current")
                # print(f"{account_type} Select Successfully.")
                write_file("./fund_transfer_test.txt", f"{account_type} Select Successfully.")

        except Exception as e:
            print("Account Field Exception:", type(e).__name__)

        try:
            # Step 5: Find Transfer Type
            transfer_type_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#transfer_type")))
            # Step 6: Select Transfer Type
            transfer_type_field = Select(transfer_type_field)

            if transfer_type == "standard":
                transfer_type_field.select_by_value("standard")
                # print(f"{transfer_type} Select Successfully.")
                write_file("./fund_transfer_test.txt", f"{transfer_type} Select Successfully.")
            if transfer_type == "express":
                transfer_type_field.select_by_value("express")
                # print(f"{transfer_type} Select Successfully.")
                write_file("./fund_transfer_test.txt", f"{transfer_type} Select Successfully.")
            if transfer_type == "international":
                transfer_type_field.select_by_value("international")
                # print(f"{transfer_type} Select Successfully.")
                write_file("./fund_transfer_test.txt", f"{transfer_type} Select Successfully.")

        except Exception as e:
            print("Transfer Type Field Exception:", type(e).__name__)

        try:
            # Step 7: Find Transfer Amount
            transfer_amount_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#transfer_amount")))
            # Step 8: Enter Transfer Amount
            transfer_amount_field.send_keys(amount)
            # print("Enter Transfer Amount Successfully.")
            write_file("./fund_transfer_test.txt", "Enter Transfer Amount Successfully.")

        except Exception as e:
            print("Transfer Amount Field Exception:", type(e).__name__)

        try:
            # Step 9: Find Transfer Button
            transfer_button = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
            # Step 10: Enter Transfer Amount
            transfer_button.click()
            # print("Transfer Button clicked Successfully.")
            write_file("./fund_transfer_test.txt", "Transfer Button clicked Successfully.")
            time.sleep(3)

        except Exception as e:
            print("Transfer Button Field Exception:", type(e).__name__)

        # Amount Verify
        try:
            # Step 11: Find Transfer Amount
            amount_result = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class] p:nth-of-type(3)")))

            assert expected_amount in amount_result.text, f"Amount Mismatch"
            # print("Amount Verify Success.")
            write_file("./fund_transfer_test.txt", "Amount Verify Success.")
            time.sleep(3)

        except Exception as e:
            print("Transfer Amount Result Exception:", type(e).__name__)

    except Exception as e:
        print("Fund Transfer page Exception:", type(e).__name__)


# Test case 1
test_fund_transfer("savings", "express", 500, "Total Amount: $505.0")



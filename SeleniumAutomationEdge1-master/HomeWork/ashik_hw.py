import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_login(username, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        assert "OrangeHRM" in driver.title, f"It's not Login page. Title Mismatch"
        print("Login page Open Successful.")
        try:
            username_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
            username_field.send_keys(username)
        except Exception as e:
            print("Username field Exception: ", type(e).__name__)

        try:
            password_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
            password_field.send_keys(password)
        except Exception as e:
            print("Password field Exception: ", type(e).__name__)

        try:
            login_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
            login_button.click()
        except Exception as e:
            print("Login button Exception: ", type(e).__name__)

        driver.execute_script('alert("Login Success !!!");')
        driver.get_screenshot_as_file("E:\\PnT_Edge_01\\Projects\\SeleniumAutomationEdge1\\Screenshots\\success_login"
                                      ".png")

        # Verify login or not
        assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" in driver.current_url, f"Login failed."
        print("Login Successful.")

        # Click My Info
        try:
            my_info_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(6) > .oxd-main-menu-item")))
            my_info_button.click()
        except Exception as e:
            print("My Info button Exception: ", type(e).__name__)

        # Verify Personal Detail page open or not
        assert "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7" in driver.current_url, f"Personal Detail page failed."
        print("Personal Detail page open Successful.")

        # First Name
        try:
            firstname_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='firstName']")))

            firstname_field.send_keys(Keys.CONTROL + 'a')
            firstname_field.send_keys(Keys.BACKSPACE)
            firstname_field.send_keys('Johan')
        except Exception as e:
            print("Firstname field Exception: ", type(e).__name__)

        # Middle Name
        try:
            middlename_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='middleName']")))
            middlename_field.send_keys(Keys.CONTROL + 'a')
            middlename_field.send_keys(Keys.BACKSPACE)
            middlename_field.send_keys('Johan')
        except Exception as e:
            print("Middlename field Exception: ", type(e).__name__)

        # Last Name
        try:
            lastname_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='lastName']")))
            lastname_field.send_keys(Keys.CONTROL + 'a')
            lastname_field.send_keys(Keys.BACKSPACE)
            lastname_field.send_keys('Ali')
        except Exception as e:
            print("Lastname field Exception: ", type(e).__name__)

        # Nickname field
        try:
            nickname_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".orangehrm-edit-employee-content .oxd-form-row:nth-of-type(1) [class='oxd-grid-3 orangehrm-full-width-grid'] input")))
            nickname_field.clear()
            nickname_field.send_keys('Khan')
        except Exception as e:
            print("Nickname field Exception: ", type(e).__name__)

        # Employee id field
        try:
            employee_id_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > .oxd-input-field-bottom-space.oxd-input-group  .oxd-input")))
            employee_id_field.clear()
            employee_id_field.send_keys('1001')
        except Exception as e:
            print("Employee id field Exception: ", type(e).__name__)

        # Other id field
        try:
            other_id_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".orangehrm-edit-employee-content .oxd-form-row:nth-child(3) [class='oxd-grid-3 orangehrm-full-width-grid']:nth-of-type(1) .oxd-grid-item--gutters:nth-of-type(2) input")))
            other_id_field.clear()
            other_id_field.send_keys('2001')
        except Exception as e:
            print("Other id field Exception: ", type(e).__name__)

        # Drivers license number field
        try:
            drivers_license_number_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1) > .oxd-input-field-bottom-space.oxd-input-group  .oxd-input")))
            drivers_license_number_field.send_keys(Keys.CONTROL + 'a')
            drivers_license_number_field.send_keys(Keys.BACKSPACE)
            drivers_license_number_field.send_keys('12345688')
        except Exception as e:
            print("Drivers license number field Exception: ", type(e).__name__)

        # License Expiry Date
        try:
            license_expiry_date_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-form-row:nth-child(3) [placeholder]")))
            license_expiry_date_field.send_keys(Keys.CONTROL + 'a')
            license_expiry_date_field.send_keys(Keys.BACKSPACE)
            license_expiry_date_field.send_keys('2023-06-15')
        except Exception as e:
            print("License Expiry Date field Exception: ", type(e).__name__)

        # SSN number field
        try:
            ssn_number_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "div:nth-of-type(3) > div:nth-of-type(1) > .oxd-input-field-bottom-space.oxd-input-group  .oxd-input")))
            ssn_number_field.clear()
            ssn_number_field.send_keys('14784757')
        except Exception as e:
            print("SSN number field Exception: ", type(e).__name__)

        # SIN number field
        try:
            sin_number_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "div:nth-of-type(3) > div:nth-of-type(2) > .oxd-input-field-bottom-space.oxd-input-group  .oxd-input")))
            sin_number_field.clear()
            sin_number_field.send_keys('14784757')
        except Exception as e:
            print("SIN number field Exception: ", type(e).__name__)

        # Nationality
        try:
            nationality = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div")))

            nationality.click()
            time.sleep(3)

            while nationality.text != "Bangladeshi":
                nationality.send_keys(Keys.ARROW_DOWN)

            nationality.send_keys(Keys.ENTER)

        except Exception as e:
            print("Nationality field Exception: ", type(e).__name__)

        # Date of birth field
        try:
            date_of_birth_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-form-row:nth-child(5) [placeholder]")))
            date_of_birth_field.send_keys(Keys.CONTROL + 'a')
            date_of_birth_field.send_keys(Keys.BACKSPACE)
            date_of_birth_field.send_keys('2020-06-15')
        except Exception as e:
            print("Date of birth field Exception: ", type(e).__name__)

        # Gender field: Female
        try:
            gender_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div > div.--gender-grouped-field > div:nth-child(2) > div:nth-child(2) > div")))
            gender_field.click()
            time.sleep(5)
            print("gender female selected.")
        except Exception as e:
            print("Gender field Exception: ", type(e).__name__)

        # Military service field
        try:
            military_service_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".orangehrm-edit-employee-content .oxd-form-row:nth-child(7) .oxd-grid-item--gutters:nth-of-type(1) input")))
            military_service_field.clear()
            military_service_field.send_keys('employ')

        except Exception as e:
            print("Military service field Exception: ", type(e).__name__)

        # Smoker field
        try:
            smoker_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".oxd-input-field-bottom-space.oxd-input-group  .oxd-checkbox-wrapper")))
            print(smoker_field.is_displayed())
            smoker_field.click()
            time.sleep(5)
        except Exception as e:
            print("Smoker field Exception: ", type(e).__name__)
            time.sleep(5)

    except Exception as e:
        print("Login page Exception: ", type(e).__name__)

    time.sleep(5)

    element_text = driver.find_element(By.CSS_SELECTOR, ".login-form > .text-center.title > b").text
    assert "ENTER ACCOUNT INFORMATION" in element_text


test_login("Admin", "admin123")

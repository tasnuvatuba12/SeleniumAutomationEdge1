import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from common import write_file


def user_Pass_Check(username, password, employ_first, middle_name, last_name):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    try:
        # Title Url
        assert "OrangeHRM" in driver.title, f"title is mismatch"
        # print("Login page open successfully")
        write_file("./report.txt", f"Login page open successfully")
        # for User field
        try:
            username_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

            username_field.send_keys(username)
            print("Username is enabled")
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        # for Password field
        try:
            password_field = WebDriverWait(driver, 15, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password'")))
            password_field.send_keys(password)
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        # for Button
        try:
            button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))

            button.click()
            print("login success")
        except Exception as e:
            print("Exception login Type:", type(e).__name__)
        # for next page Open Url
        assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" in driver.current_url, f"dont match"
        time.sleep(3)
        print("login Page open")
        # for menu button
        try:
            my_info_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".oxd-sidepanel-body .oxd-main-menu-item-wrapper:nth-of-type(6) .oxd-main-menu-item")))

            my_info_button.click()
            print("info success")


        except Exception as e:
            print("Exception login Type:", type(e).__name__)
        """try:
            assert "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7" in driver.current_url,f"dont match"

            driver.find_element_by_xpath("//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']"). send_keys("Selenium")
            driver.find_element_by_xpath("//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").clear()
            print("clear success")
        except Exception as e:
            print("Exception login Type:",type(e).__name__)
            """
        # Menu buttons Page profile field
        try:
            employ_first_name = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='firstName']")))

            employ_first_name.send_keys(employ_first)
            print("employed first field is enabled")
            time.sleep(5)
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        # Menu buttons Page profile field
        try:
            employ_middle_name = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='middleName']")))

            employ_middle_name.send_keys(middle_name)
            print("employed middle field is enabled")
            time.sleep(5)
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        # Menu buttons Page profile field
        try:
            employ_last_name = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='lastName']")))

            employ_last_name.send_keys(last_name)
            print("employed middle field is enabled")
            time.sleep(5)
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        # nationality
        try:
            nationality_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "oxd-select-text-input")))

            nationality_field = Select(nationality_field)
            nationality_field.select_by_value("Algerian")
            print("selected success")
            time.sleep(5)
        except Exception as e:
            print("Exception Type: ", type(e).__name__)

        # menu buttons Profile Save button
        try:
            prifile_Save_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) .oxd-button--secondary")))

            prifile_Save_button.click()
            print("Save success")
            time.sleep(20)

        except Exception as e:
            print("Exception login Type:", type(e).__name__)

    except Exception as e:
        print("Logon page Exception:", type(e).__name__)


user_Pass_Check("admin", "admin123", "amir", "hossain", "ritu")
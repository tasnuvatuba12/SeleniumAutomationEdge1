import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def alert_demo():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    '''
    # normal alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button").click()
    time.sleep(5)
    driver.switch_to.alert.accept()  # Click on Ok
    time.sleep(3)
    
    # confirm alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button").click()
    time.sleep(5)
    driver.switch_to.alert.dismiss()  # Click on Cancel
    time.sleep(3)

    # prompt alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button").click()
    time.sleep(5)
    driver.switch_to.alert.send_keys("Test Automation")
    driver.switch_to.alert.accept()
    time.sleep(3)
    '''
    driver.execute_script('alert("Login Success !!!");')
    try:
        driver.get_screenshot_as_file("E:\\PnT_Edge_01\\Projects\\SeleniumAutomationEdge1\\Screenshots\\success_login"
                                      ".png")
    except Exception as e:
        print("Exception")
        time.sleep(4)


alert_demo()

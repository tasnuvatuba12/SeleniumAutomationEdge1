import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def multiple_window_demo():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    driver.find_element(By.LINK_TEXT, 'Click Here').click()

    # switch to new tab
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://google.com")
    time.sleep(4)

    # back to previous tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)


multiple_window_demo()

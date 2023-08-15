import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def mouse_hover_demo():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/")

    try:
        desktops = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))
        all_actions = ActionChains(driver)
        all_actions.move_to_element(desktops).perform()
    except Exception as e:
        print("desktops Exception: ", type(e).__name__)

    try:
        mac_1 = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Mac (1)")))
        mac_1.click()
    except Exception as e:
        print(" Mac (1) Exception: ", type(e).__name__)


mouse_hover_demo()

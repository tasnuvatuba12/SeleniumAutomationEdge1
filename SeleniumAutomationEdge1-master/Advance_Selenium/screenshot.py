import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def capture_screenshot():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com")

    driver.get_screenshot_as_file("E:\\PnT_Edge_01\\Projects\\SeleniumAutomationEdge1\\Screenshots\\demo2.png")


capture_screenshot()

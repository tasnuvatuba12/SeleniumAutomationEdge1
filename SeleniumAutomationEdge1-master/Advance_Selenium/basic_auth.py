from selenium import webdriver


def basic_auth_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # protocol://username:password@url
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


basic_auth_demo()

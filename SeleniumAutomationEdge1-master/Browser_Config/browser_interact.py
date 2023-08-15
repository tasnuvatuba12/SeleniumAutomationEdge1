import time
from selenium import webdriver


def launch_website(browser_name, url):
    # Browser launch
    # Create a new Chrome instance
    try:
        if browser_name.lower() == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif browser_name.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser_name.lower() == 'edge':
            driver = webdriver.Edge()
            driver.maximize_window()

        try:
            driver.get(url)
        # driver.set_window_size(900, 500)
            time.sleep(3)
        except Exception as e:
            print("Failed to launch.Invalid URL: %s" % url)

    except Exception as e:
        print("Exception Type: ", type(e).__name__)

"""
launch_website("Chrome", "http://google.com")
launch_website("firefox", "http://google.com")
launch_website("edge", "http://google.com")
"""


browser_list = ['chrome']

for select_browser_name in browser_list:
    launch_website(select_browser_name, "https://google.com")


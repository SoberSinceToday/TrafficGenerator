from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def createDriver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5.00)
    driver.set_page_load_timeout(5.00)
    return driver

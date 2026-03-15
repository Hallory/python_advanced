import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox") 
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
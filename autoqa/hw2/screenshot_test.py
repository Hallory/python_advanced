from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_screenshot(driver):
    wait = WebDriverWait(driver, 15)

    driver.get("https://itcareerhub.de/ru")

    payment_section = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-artboard-recid="1921734713"]')
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", payment_section
    )

    payment_section.screenshot("payment_methods.png")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
NEEDED_TEXT = "semper posuere integer et senectus justo curabitur."


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


def test_text_in_iframe(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    frames = driver.find_elements(By.TAG_NAME, "iframe")
    assert frames, "No frames found"

    driver.switch_to.frame(frames[0])

    body = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    assert NEEDED_TEXT in body.text
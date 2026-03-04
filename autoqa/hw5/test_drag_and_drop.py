import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.globalsqa.com/demo-site/draganddrop/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()
    

def dismiss_cookie_banner(driver):
    driver.execute_script("""
        const banner = document.querySelector('.fc-consent-root');
        if (banner) banner.remove();

        const backdrop = document.querySelector('.fc-dialog-overlay, .fc-overlay, .fc-backdrop');
        if (backdrop) backdrop.remove();

        document.documentElement.style.overflow = 'auto';
        document.body.style.overflow = 'auto';
    """)

def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    dismiss_cookie_banner(driver)


    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(frame)

    source = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))[0]
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    ActionChains(driver).drag_and_drop(source, trash).perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3

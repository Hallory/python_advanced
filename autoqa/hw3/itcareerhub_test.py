import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://itcareerhub.de/ru"


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


def test_itcareerhub(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    logo = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'img[alt="IT Career Hub"]')
        )
    )
    assert logo.is_displayed()

    programs = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Программы"))
    )
    assert programs.is_displayed()

    payment = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Способы оплаты"))
    )
    assert payment.is_displayed()

    about = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "О нас"))
    )
    assert about.is_displayed()

    reviews = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Отзывы"))
    )
    assert reviews.is_displayed()

    blog = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Блог"))
    )
    assert blog.is_displayed()

    lang_ru = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "ru"))
    )
    assert lang_ru.is_displayed()

    lang_de = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "de"))
    )
    assert lang_de.is_displayed()

    driver.get("https://itcareerhub.de/ru/contact-us")

    call_text = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[field="tn_text_1709210712463"]')
        )
    )
    
    assert "Хотите записаться на курс и получить помощь по вопросам обучения?" in call_text.text
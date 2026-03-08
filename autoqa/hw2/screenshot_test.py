from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://itcareerhub.de/ru")
    driver.maximize_window()

    payment_section = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-artboard-recid="1921734713"]')
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", payment_section
    )

    payment_section.screenshot("payment_methods.png")

finally:
    driver.quit()
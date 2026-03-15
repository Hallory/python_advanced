from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_checkout_total(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)

    login_page.open_page(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_backpack_to_cart()
    inventory_page.add_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_info_page.fill_checkout_info("John", "Doe", "12345")
   
    checkout_info_page.click_continue()
    print("Current URL", driver.current_url)
    
    total = checkout_overview_page.get_total_value()
    assert total == "58.29", f"Expected total to be 58.29, but got {total}"
    
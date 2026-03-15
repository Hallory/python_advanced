from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        return self.click(self.CHECKOUT_BUTTON)
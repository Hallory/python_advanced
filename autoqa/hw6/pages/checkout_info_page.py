from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    FIRST_NAME_FIELD = (By.ID,"first-name")
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_FIELD, first_name)
        self.type(self.LAST_NAME_FIELD, last_name)
        self.type(self.POSTAL_CODE_FIELD, postal_code)
        
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
        
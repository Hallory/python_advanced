from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    
    def get_total_value(self):
        total_text = self.get_text(self.SUMMARY_TOTAL)
        return total_text.split("$")[1]


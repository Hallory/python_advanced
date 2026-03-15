from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_BUTTON)
        
    def add_tshirt_to_cart(self):
        self.click(self.TSHIRT_BUTTON)
        
    def add_onesie_to_cart(self):
        self.click(self.ONESIE_BUTTON)
        
    def open_cart(self):
        self.click(self.CART_LINK)
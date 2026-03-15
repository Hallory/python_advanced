from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        

    def open(self, url):
        return self.driver.get(url)

    
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    
    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    
    def click(self, locator):
        element = self.find(locator)
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        
        self.driver.execute_script("arguments[0].click();", element)
    
    
    def type(self, locator, text):
        print("type",locator, text)
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        
        
    def get_text(self, locator):
        return self.find(locator).text
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.item_rollerblade = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@alt,'Rollerblade Hombre')]")))

    def select_rollerblade(self):
        self.item_rollerblade.click()

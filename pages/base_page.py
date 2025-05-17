import time
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        element = self.wait.until(ec.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def scroll_down(self, times):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(2)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def take_screenshot(self, file_name):
        self.driver.save_screenshot("screenshots/" + file_name + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".png")
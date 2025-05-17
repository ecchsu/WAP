from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.browse_page import BrowsePage

class Homepage(BasePage):

    BROWSE_TAB = (By.LINK_TEXT, "Browse")

    def click_browse_tab(self):
        self.click(self.BROWSE_TAB)
        return BrowsePage(self.driver)



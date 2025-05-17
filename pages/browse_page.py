from pages.base_page import BasePage
from pages.streamer_page import StreamerPage
from selenium.webdriver.common.by import By

class BrowsePage(BasePage):

    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    VIDEO_LINK = (By.XPATH, "//h2[text()='VIDEOS']/ancestor::div/following-sibling::div//a[contains(@href, '/videos/')]")

    def search_keyword(self, keyword):
        """
        Click on the search field and enter the search keyword
        """
        self.click(self.SEARCH_FIELD)
        self.send_keys(self.SEARCH_FIELD, keyword + "\n")

    def select_video(self):
        """
        Select the first video on the Browse Page Video section
        """
        video = self.find(self.VIDEO_LINK)
        if video:
            self.click(video)
            return StreamerPage(self.driver)
        else:
            raise Exception("No video found on Browse Page in Videos category")

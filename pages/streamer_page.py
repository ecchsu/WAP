import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class StreamerPage(BasePage):

    def is_video_playing(self):
        """
        Check if the video is playing by checking the readyState
        """
        return self.driver.execute_script("""
            const video = document.querySelector('video');
            return video && !video.paused && !video.ended && video.readyState > 2;
        """)

    def wait_for_video_to_be_ready(self, max_attempts=3, interval=2):
        """
        Polls the video readyState every `interval` seconds,up to `max_attempts` times.
        """
        for attempt in range(max_attempts):
            try:
                state = self.driver.execute_script("""
                    const video = document.querySelector('video');
                    return video ? video.readyState : 0;
                """)

                if state >= 3:
                    break
                else:
                    print(f"Attempt {attempt + 1}: Video not ready yet (readyState={state})")
            except Exception as e:
                print(f"Attempt {attempt + 1}: Error when checking video state - {e}")

            time.sleep(interval)

    def close_modal_if_present(self):
        try:
            modal_close_button = self.wait.until(
                ec.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@aria-label, 'Close') or contains(@class, 'close')]"))
            )
            self.click(modal_close_button)
            time.sleep(1)
        except TimeoutException:
            print("No modal appeared.")
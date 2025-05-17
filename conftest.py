import os

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver(request):
    url = "https://m.twitch.tv"
    os.makedirs("screenshots", exist_ok=True)
    driver = webdriver.Chrome()
    driver.set_window_size(400, 800)
    driver.get(url)
    yield driver
    driver.quit()
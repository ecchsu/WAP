from pages.homepage import Homepage

def test_search_and_stream(driver):
    """
        Test the search and video playback flow on the Twitch mobile webpage.

        Steps:
        1. Navigate to the homepage and click the 'Browse' tab.
        2. Search for the keyword "StarCraft II".
        3. Scroll down the search results and select the first video from the results.
        5. Close any modal if present before proceeding.
        6. Verify the video is playing.
        """
    homepage = Homepage(driver)
    browse_page = homepage.click_browse_tab()
    browse_page.search_keyword("StarCraft II")
    browse_page.scroll_down(times=2)
    streamer_page = browse_page.select_video()
    streamer_page.close_modal_if_present()
    streamer_page.wait_for_video_to_be_ready(max_attempts=2, interval=1)
    streamer_page.take_screenshot("streamer_page_video_playing")
    assert streamer_page.is_video_playing(), "Video is not playing"

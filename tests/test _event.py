import pytest
from pages.home_page import HomePage
from pages.events_page import EventsPage
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("driver")
class TestEventPage:

    def test_event_page_loads(self, driver):
        home = HomePage(driver)
        event = EventsPage(driver)


        home.open_url("https://www.swasthyawarriors.com/")
        assert home.is_home_page_loaded(), "Homepage did not load"


        home.click_element((BY.LINK_TEXT, "Events"))
        assert event.is_event_page_loaded(), "Event page did not load"


        count = event.get_event_count()
        print(f"Number of events displayed: {count}")
        assert count > 0, "No events are displayed"




from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse
import time

class BasePage():

    PAGE_LOAD_WAIT_INTERVAL = 2
    PAGE_LOAD_COUNTER = 5

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        """
        To navigate to respective url passed
        """
        self.driver.get(url)
        self.wait_for_page_to_load()

    def get_current_url_path(self):
        """
        Returns the current url path the page
        Input : N/A
        Output : String
        """
        url = self.driver.current_url
        url = urlparse(url)
        return url.path

    def wait_for_page_to_load(self):
        """
        Waits for the page to Load completely
        if Page takes more than Counter*Interval, it raises an Expection 
        """
        counter = self.PAGE_LOAD_COUNTER
        while(counter > 0):
            page_state = self.driver.execute_script('return document.readyState;' ) 
            if(page_state == 'complete'): return True
            time.sleep(self.PAGE_LOAD_WAIT_INTERVAL)
            counter-=1
        raise Exception("Timeout! Page taking long time to load")


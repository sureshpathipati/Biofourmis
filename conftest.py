import pytest
from config.browser_setup import browser_setup
from pages.bio_fourmis_page import BioFourmisPage

DEFAULT_TIMEOUT = 10

@pytest.fixture(scope='session')
def setUp(request):
	driver = browser_setup()
	driver.implicitly_wait(DEFAULT_TIMEOUT)
	driver.set_page_load_timeout(20)
	bfs = BioFourmisPage(driver)
	yield bfs
	driver.quit()

def take_screenshot(request):
	driver.save_screenshot(request.node.name)
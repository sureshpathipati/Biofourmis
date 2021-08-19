from pages.base_page import BasePage

class AboutusPage(BasePage):
		def __init__(self, driver):
				self.driver = driver

		def navigate_to_aboutus_page(self):
				self.driver.find_element_by_id('about').click()
				self.wait_for_page_to_load()

		def is_aboutus_page(self):
				if self.aboutus_url_path() != '/about-us/':
						return False 
				return self.driver.find_element_by_class_name('active-page').get_attribute('id') == 'about'

		def aboutus_url_path(self):
				return self.get_current_url_path()
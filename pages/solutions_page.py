from pages.base_page import BasePage

class SolutionsPage(BasePage):
		def __init__(self, driver):
				self.driver = driver

		def navigate_to_solutions_page(self):
				self.driver.find_element_by_id('solutions').click()
				self.wait_for_page_to_load()

		def is_solutions_page(self):
				if self.soultions_url_path() != '/solutions/':
						return False 
				return self.driver.find_element_by_class_name('active-page').get_attribute('id') == 'solutions'

		def soultions_url_path(self):
				return self.get_current_url_path()
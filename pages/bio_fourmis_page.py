from pages.base_page import BasePage
from pages.solutions_page import SolutionsPage

class BioFourmisPage:
	def __init__(self, driver):
		self.driver = driver

	def base_page(self):
		return BasePage(self.driver)

	def solutions_page(self):
		return SolutionsPage(self.driver)

	def quit_browser(self):
		return self.driver.quit()
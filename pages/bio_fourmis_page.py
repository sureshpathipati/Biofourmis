from pages.base_page import BasePage


class BioFourmis:
	def __init__(self, driver):
		self.driver = driver

	def base_page(self):
		return BasePage(self.driver)

	def quit_browser(self):
		return self.driver.quit()
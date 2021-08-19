from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent

def browser_setup():
    return chrome_browser()

def chrome_browser():
    return Chrome(executable_path=parent_dir+'/drivers/chromedriver')
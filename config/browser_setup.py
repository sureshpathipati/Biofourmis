from selenium import webdriver
from pathlib import Path
import os

parent_dir = Path(__file__).resolve().parent.parent

def browser_setup():
    if os.environ['BROWSER_NAME'] == 'chrome':
        return chrome_browser()
    return firefox_browser()

def chrome_browser():
    return webdriver.Chrome()

def firefox_browser():
    return webdriver.Firefox()
from selenium import webdriver
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent

def browser_setup():
    return chrome_browser()

def chrome_browser():
    return webdriver.Chrome()
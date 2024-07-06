from selenium import webdriver
from IgnitionAutomationTools.Pages.PerspectivePageObject import PerspectivePageObject


with webdriver.Chrome() as web_driver:
    page = PerspectivePageObject(web_driver, 'http://localhost:8088', '/Testing')

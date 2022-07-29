import ddt
from ddt import ddt, data, unpack
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from Methods.selenium_driver import SeleniumDriver
baseUrl = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)

from selenium import webdriver
from Methods import custom_logger
import logging
from Methods.selenium_driver import SeleniumDriver

test = SeleniumDriver.getWebDriverInstanc1e("Chrome")
print(test.title)
log = custom_logger.customLogger(logLevel=logging.DEBUG)
log.error(" ### TEST FAILED")
SeleniumDriver.screenShot(test,"lo")
from Methods.selenium_driver import SeleniumDriver
import os,time


def test_demo():
    driver = SeleniumDriver.getWebDriverInstanc1e("Chrome", "https://easebuzz.in/")
    SeleniumDriver.elementClick(driver,"//a[@class='sign-up']")
    time.sleep(5)
    info = SeleniumDriver.Readtext(driver,"//p[@class='section-info']")
    SeleniumDriver.sendKeys(driver,info,"//input[@id='fullname']")
    time.sleep(10)

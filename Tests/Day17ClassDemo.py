"""
1: Open URL
2 : Enter Login ID
3 :  Enter Password
4 : click on Login

"""
from Methods.selenium_driver import SeleniumDriver
from Methods.Easebuzz import login, Benifi
import os

def test_keyword():

    driver = SeleniumDriver.getWebDriverInstanc1e("Chrome", "https://courses.letskodeit.com/login")

    SeleniumDriver.sendKeys(driver,"rathore.nilesh1489@gmail.com","xpath",'//*[@placeholder="Email Address"]')
    SeleniumDriver.sendKeys(driver,"12345", "xpath", '//*[@id="password"]')
    SeleniumDriver.elementClick(driver,"xpath", '//*[@value="Login"]')


os.system("")


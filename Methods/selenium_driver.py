from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import Methods.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():


    def __init__(self, driver):
        self.driver = driver

    def Verify_title(driver,titleToBeVerify):
        currentTitle = driver.title
        print(currentTitle)
        print(titleToBeVerify)

        if currentTitle == titleToBeVerify:
            cl.customLogger().info("We have verified title & its expected")
            print("correct")
        else:
            cl.customLogger().error("We have verified that titles are not correct or we are on wrong page")
            print("wrong")
    def openURL(driver,URL):
        driver.get(URL)
        cl.customLogger().info("we are able to Open URL " + URL)

    def getWebDriverInstanc1e(browser, baseURL):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        # browser = "firefox"
        # baseURL = "https://letskodeit.teachable.com/"
        if browser == "Edge":
            # Set ie driver
            driver = webdriver.Edge()
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)

        return driver


    def screenShot(driver, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        log = cl.customLogger(logging.DEBUG)

        fileName = resultMessage + "_" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C://DDFramework//screenshots//"
        relativeFileName = screenshotDirectory + fileName


        try:
            if not os.path.exists(screenshotDirectory):
                os.makedirs(screenshotDirectory)
            print("1")
            driver.save_screenshot(relativeFileName)
            print("2")
            log.info("Screenshot save to directory: " + relativeFileName)
        except:
            cl.customLogger(logging.DEBUG).error("### Exception Occurred when taking screenshot")
            # print_stack()

    def openURL(self, url):
        self.get(url)
        cl.customLogger().info("### User is abble to open " + url)

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            cl.customLogger().info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator_value):
        element = None
        try:
            element = self.find_element(By.XPATH, locator_value)
            cl.customLogger().info("Element found with locator: " +  "xpath" +
                          " and  locatorType: " + locator_value)
        except:
            cl.customLogger().info("Element not found with locator: " +  "xpath" +
                          " and  locatorType: " + locator_value)
        return element

    def elementClick(self, locator_value):
        try:
            element = self.find_element(By.XPATH, locator_value)
            element.click()
            cl.customLogger().info("Clicked on element with locator: " +  "xpath" +
                          " locatorType: " + locator_value)
        except:
            cl.customLogger().info("Cannot click on the element with locator: " +  "xpath" +
                          " locatorType: " + locator_value)

    def sendKeys(self, data,  locator_value):
        try:
            element = self.find_element(By.XPATH, locator_value)
            element.send_keys(data)
            cl.customLogger().info("Sent data on element with locator: " +  "xpath" +
                          " locatorType: " + locator_value)
        except:
            cl.customLogger().info("Cannot send data on the element with locator: " +  "xpath" +
                  " locatorType: " + locator_value)


    def isElementPresent(self, locatorType="id"):
        try:
            element = self.getElement(locatorType)
            if element is not None:
                cl.customLogger().info("Element present with locator: " + "xpath" +
                              " locatorType: " + locatorType)
                return True
            else:
                cl.customLogger().info("Element not present with locator: " + "xpath" +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator_value):
        try:
            elementList = self.driver.find_elements(By.XPATH,locator_value)
            if len(elementList) > 0:
                cl.customLogger().info("Element present with locator: " +  "xpath" +
                              " value : " + str(locator_value))
                return True
            else:
                cl.customLogger().info("Element not present with locator: " +  "xpath" +
                              " value: " + str(locator_value))
                return False
        except:
            cl.customLogger().info("Element not found")
            return False

    def waitForElement(self, timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(By.XPATH)
            cl.customLogger().info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            # wait = WebDriverWait(self.driver, 10, poll_frequency=1,
            #                      ignored_exceptions=[NoSuchElementException,
            #                                          ElementNotVisibleException,
            #                                          ElementNotSelectableException]
            # element = wait.until(EC.element_to_be_clickable((byType,
            #                                                  "stopFilter_stops-0"))
            cl.customLogger().info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def dragdrop(self,dragxpath,dropxpath):
        fromElement = self.find_element(By.XPATH, dragxpath)
        toElement = self.find_element(By.XPATH, dropxpath)
        time.sleep(2)
        try:
            actions = ActionChains(self)
            actions.drag_and_drop(fromElement, toElement).perform()
            # actions.click_and_hold(fromElement).move_to_element(toElement).releasd).perform()
            cl.customLogger().info("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            cl.customLogger().info("Drag And Drop failed on element")

    def selectby(self,XpathElement,Type,value):
        x=SeleniumDriver.getElement(self,XpathElement)
        sel = Select(x)
        if Type.lower() == "value":
            sel.select_by_value(value)
        if Type.lower() == "visible":
            sel.select_by_visible_text(value)
        if Type.lower() == "index":
            sel.select_by_index(value)

    def closebrowser(self):
        self.closebrowser()
        cl.customLogger().info("we are closing our browser")

    def getvalue(self, xpathelement,property):
        x = SeleniumDriver.getElement(self, xpathelement)
        if property == "text":
            y = x.text
        else:
            y = x.get_attribute(property)

        cl.customLogger().info("getting " + property + " value from " + xpathelement )
        return y

    def selectbyVal(self,XpathElement,value):
        x=SeleniumDriver.getElement(self,XpathElement)
        sel = Select(x)
        sel.select_by_value(value)

    def selectbyText(self,XpathElement,value):
        x=SeleniumDriver.getElement(self,XpathElement)
        sel = Select(x)
        sel.select_by_visible_text(value)

    def selectbyIndex(self,XpathElement,value):
        x=SeleniumDriver.getElement(self,XpathElement)
        sel = Select(x)
        sel.select_by_index(value)

    def Readtext(self, xpathelement):
         x = SeleniumDriver.getElement(self, xpathelement).text
         cl.customLogger().info("getting  Text from " + xpathelement )
         return x

    def getAttributee(self, xpathelement,property):
        x = SeleniumDriver.getElement(self, xpathelement)
        y = x.get_attribute(property)
        cl.customLogger().info("getting " + property + " value from " + xpathelement )
        return y
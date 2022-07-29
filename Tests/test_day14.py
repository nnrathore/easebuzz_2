from Methods.selenium_driver import SeleniumDriver
from Methods.custom_logger import customLogger

test = SeleniumDriver.getWebDriverInstanc1e("Chrome","https://courses.letskodeit.com/practice")
print(test.title)



#
# customLogger().critical("this msg is for info")
#
# SeleniumDriver.selectby(driver,'//select[@id="carselect"]',"value","benz")
#
# SeleniumDriver.openURL(driver,"https://jqueryui.com/droppable/")
# driver.implicitly_wait(3)
#
# driver.switch_to.frame(0)
# SeleniumDriver.dragdrop(driver,'//div[@id="draggable"]','//div[@id="droppable"]')
# print("done")
#

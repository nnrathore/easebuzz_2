from selenium import webdriver

def test_demo1():
    driver = webdriver.Chrome()

    driver.implicitly_wait(3)
    # Maximize the window
    driver.maximize_window()
    # Loading browser with App URL
    driver.get("https://courses.letskodeit.com/practice")


def test_demo2():
    driver = webdriver.Chrome()
    # else:
    #     driver = webdriver.Firefox()
    # Setting Driver Implicit Time out for An Element
    driver.implicitly_wait(3)
    # Maximize the window
    driver.maximize_window()
    # Loading browser with App URL
    driver.get("https://courses.letskodeit.com/practice")

def test_demo3():
    driver = webdriver.Chrome()
    # else:
    #     driver = webdriver.Firefox()
    # Setting Driver Implicit Time out for An Element
    driver.implicitly_wait(3)
    # Maximize the window
    driver.maximize_window()
    # Loading browser with App URL
    driver.get("https://courses.letskodeit.com/practice")
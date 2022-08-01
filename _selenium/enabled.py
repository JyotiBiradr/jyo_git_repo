#check if the element is enabled or not
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
driver = Chrome(r"./chromedriver.exe")
driver.get("file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/loading.html")
driver.maximize_window()
class _visibility_of_element_located(visibility_of_element_located):

    def __call__(self,locator):
        print("Calling __call__method of Child class")
        result=super().__call__(driver)
        if isinstance(result,WebElement):
            # extra functionality that we are adding in the child class
            #checking for enablement of the element
            return result.is_enabled()
            sleep(3)
        else:
            return False
w=WebDriverWait(driver,20)
v=_visibility_of_element_located(('name','fname'))
sleep(8)
w.until(v)
driver.find_element_by_name("fname").send_keys("hello")

print("Done")



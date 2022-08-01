#decorators using in selenium2
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import  Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver=Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(4)
#check if the element is loaded in the dom
#check if the element is loaded in the webpage
#check if the element is enabaled
class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)#initialising parent class constructor
    #overridding parent __call__ method of  parent class
    def __call__(self, driver):
        print("calling __call__ method of child class")
        result=super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False
def _wait(func):
    def wrapper(*args,**kwargs):
        locator=args[0] # args = (("link text", "Register")) [args always comes tuple]
        w=WebDriverWait(driver,20)
        v=_visibility_of_element_located(locator)
        w.until(v,message="Progress bar was not located")
            #original function get executed
        return func(*args,**kwargs)
    return wrapper
@_wait
def click_element(locator):
    driver.find_element(*locator).click() # *locator->unpacking
@_wait
def enter_text(locator,*,value):#before * are positional,after * are keyword arguments
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)
@_wait
def select_item(locator,*,item):
    element=driver.find_element(*locator)
    s=Select(element)#creating object of select class
    if isinstance(item,str):
        s.select_by_visible_text(item)
    elif isinstance(item,int):
        s.select_by_index(item ,int)
    else:
        raise Exception




click_element((By.LINK_TEXT,"Register"))
click_element((By.ID,"gender-male"))
enter_text((By.NAME, "FirstName"),value="hello")
enter_text((By.NAME, "LastName"),value="world")
enter_text((By.CSS_SELECTOR,"input[name='Email']"),value="hello.world@company.com")
enter_text((By.ID,"Password"),value="Password123")
enter_text((By.NAME,"ConfirmPassword"),value="Password123")
click_element((By.ID,"register-button"))
sleep(3)
driver.close()







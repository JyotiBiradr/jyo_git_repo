from time import sleep
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
driver=Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/progressbar.html")
driver.maximize_window()

driver.find_element_by_xpath("//button[text()='Click Me']").click()
driver.implicitly_wait(20)
try:
    ele=driver.find_element_by_name("hello world")
except NoSuchElementException:
    pass
driver.close()
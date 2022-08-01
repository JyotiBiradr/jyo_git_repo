from time import sleep
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get(r"https://www.python.org/downloads/")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Python 3.9.12']/../..//a[text()='Release Notes']").click()
sleep(2)
driver.close()
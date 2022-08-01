from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@value='Search']").click()
print(driver.switch_to.alert.text)
sleep(3)
driver.switch_to.alert.accept()
driver.close()
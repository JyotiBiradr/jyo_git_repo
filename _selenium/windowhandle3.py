from selenium.webdriver import Chrome
from time import sleep
driver=Chrome("./chromedriver.exe")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("python")
sleep(2)
driver.find_element_by_xpath("//strong[text()='Python']").click()
sleep(3)
driver.find_element_by_xpath("//input[@value='Search']").click()

driver.close()
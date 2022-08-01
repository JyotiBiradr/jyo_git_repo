from time import sleep
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/demo.html")
driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()
sleep(2)
driver.close()

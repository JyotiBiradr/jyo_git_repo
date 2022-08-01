from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
driver=Chrome("./chromedriver.exe")
driver.get(r"file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/demo.html")
driver.maximize_window()
w=WebDriverWait(driver,20)
v=visibility_of_element_located(("xpath","(//input[@type='text'])[10]"))
#v=visibility_of_element_located(("id","firstname"))#visibility _of_element always comes in tuple
w.until(v)
#driver.find_element_by_id("firstname").send_keys("hello")
driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys("hello")
sleep(3)
driver.close()

from time import sleep
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get(r"http://demowebshop.tricentis.com/login")
driver.maximize_window()
sleep(2)
ele=driver.find_element_by_class_name("ico-register")
ele.click()
#or
driver.find_element_by_link_text("Register").click()
sleep(2)
driver.find_element_by_id("Password").send_keys("hello")
sleep(1)
driver.close()
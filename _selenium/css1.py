from time import sleep
from selenium.webdriver import Chrome
driver=Chrome(r"./chromedriver.exe")
driver.get(r"file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/css_selector.html")
driver.maximize_window()
sleep(2)
driver.find_element_by_css_selector("input[class='first_row']").send_keys("hello")
#or
driver.find_element_by_css_selector("input[name='fname']").send_keys("world")
driver.find_element_by_css_selector("input[class='first_row']:nth-child(2)").send_keys("hai")#it will take next of first_or(second textbox)
sleep(2)
driver.close()


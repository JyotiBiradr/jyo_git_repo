from time import sleep
from selenium import webdriver
driver=webdriver.Chrome(r"./chromedriver.exe")
driver.get(r"file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/demo.html")
sleep(2)
driver.maximize_window()
sleep(2)
url=driver.current_url
print(url)
c_title=driver.title
print(c_title)
driver.refresh
sleep(4)
driver.forward
sleep(4)
source=driver.page_source
print(source)
driver.close()

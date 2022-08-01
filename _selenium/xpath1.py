from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver = Chrome("./chromedriver.exe")
driver.get(r"file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/demo.html")
driver.maximize_window()
links = driver.find_elements_by_xpath("//a") #/(slash should be forward slash)
images = driver.find_elements_by_xpath("//img" )
inputs=driver.find_elements_by_xpath("//input[@type='text']")
radios=driver.find_elements_by_xpath("//input[@type='radio']")
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
tables=driver.find_elements_by_xpath("//table")
sleep(2)
print(f"No of links{len(links)}")
print(f"No of images{len(images)}")
print(f"No of textboxes{len(inputs)}")
print(f"No of radio button{len(radios)}")
print(f"No of checkboxes{len(checkboxes)}")
print(f"No of tables{len(tables)}")

elements=driver.find_elements_by_xpath("//input[@name='download']")
for ele in elements:
    ele.click()
    sleep(1)
box=driver.find_element_by_id("standard_cars")
s=Select(box)# creating object of class select
all_option=s.options
items=[item.text for item in all_option]
print(items)
s.select_by_visible_text(items[-1])
sleep(2)





driver.close()

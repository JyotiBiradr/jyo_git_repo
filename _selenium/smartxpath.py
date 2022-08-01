from time import sleep
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get(r"http://demowebshop.tricentis.com/shipping-returns")
driver.maximize_window()
boxes=driver.find_elements_by_xpath("//label")
items=[item.text for item in boxes]
print(items)
for box in boxes:
    box.click()

sleep(5)
driver.close()
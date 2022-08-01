from selenium.webdriver import Chrome
from time import sleep
driver=Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Twitter']").click()

handle=driver.window_handles
print(handle)

driver.switch_to.window(handle[1])
sleep(15)
#driver.find_element_by_xpath("//a[@href='/explore']")
driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hello")
sleep(2)
driver.close()
driver.switch_to.window(handle[0])
sleep(2)
driver.find_element_by_link_text("Register").click()
sleep(2)
for handle in handle:
    print(handle)
driver.quit()


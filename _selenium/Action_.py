from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
driver=Chrome("./chromedriver.exe")
a_obj=ActionChains(driver)
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
ele=driver.find_element_by_xpath("//a[text()='Job search']")
a_obj.move_to_element(ele).perform()

ele2=driver.find_element_by_xpath("//a[text()='Jobs by Title']")
a_obj.move_to_element(ele2).perform()
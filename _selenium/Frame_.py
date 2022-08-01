from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/SANKETH/Desktop/python%20practice/selenium1/iframe.html")
driver.maximize_window()
driver.switch_to_frame("frame1")#switching  from normal page to frame1
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[text()='Register']").click()
#page within another page is frame
driver.switch_to_default_content()#take control to parent frame
driver.switch_to_frame("FR2") #switching from fram1 to frame2
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='search_form']").send_keys("abc")



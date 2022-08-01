from time import sleep
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
driver=Chrome("./chromedriver.exe")
driver.get("https://www.goibibo.com/")
driver.maximize_window()
sleep(1)
driver.find_element_by_xpath("//span[text()='Departure']").click()
#driver.find_element_by_xpath("//div[text()='July 2022']/../..//p[text()='28']").click() (composite xpath)
def select_date(month ,year,day):
    _xpath=f"//div[text()='{month} {year}']/../..//p[text()={day}]"
    for _ in range(12):
        try:
            driver.find_element_by_xpath(_xpath).click()
            return True
        except NoSuchElementException:
            driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
            sleep(2)
    return False

select_date('December', '2022',27)
driver.close()
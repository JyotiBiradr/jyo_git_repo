from excel import read_locator
from homepage import HomePage
class LoginPage(HomePage):
    def __init__(selfself,driver):
        super().__init__(driver)
        locators=read_locator("loginpage")
    def login_enter_email(self,email):
        element=LoginPage.locators['txt_email']

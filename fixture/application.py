#задание 7
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)
        self.group = GroupHelper(self)
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
    def destroy(self):
        self.wd.quit()
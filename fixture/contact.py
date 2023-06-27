#задание 7
from selenium.webdriver.support.ui import Select
class ContactHelper:
    def __init__(self, app):
        self.app = app
    def add(self, contact):
        wd = self.app.wd
        # open page "add new"
        wd.find_element_by_link_text("add new").click()
        # fill in the fields
        self.user_information(contact, wd)
        self.submit_contact_creation()
        self.app.navigation.return_to_home_page()
    def delete_first_contact(self):
        wd = self.app.wd
        # open contacts page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
    def first_contact_change(self, contact):
        wd = self.app.wd
        # open contact page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        # contact change
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.user_information(contact, wd)
        # save changes
        wd.find_element_by_name("update").click()
    def user_information(self, contact, wd):
        # first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        # last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        # address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        # email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # birthday
        # day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.day_of_birth)
        # month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.month_of_birth)
        #if contact.bmonth != '-':
          #  wd.find_element_by_xpath(f"//option[@value='{contact.bmonth}']").click()
        # year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
    def count(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        return len(wd.find_elements_by_name("selected[]"))
#задание 13
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # open contacts page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
         # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def first_contact_change(self, contact):
        self.contact_change_by_index(0)

    def contact_change_by_index(self, index, contact):
        wd = self.app.wd
        # open contact page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        # contact change
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.user_information(contact, wd)
        # save changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def contact_change_by_id(self, id, contact):
        wd = self.app.wd
        # open contact page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        xpath = f'//a[@href="edit.php?id={id}"]'
        wd.find_element_by_xpath(xpath).click()
        self.user_information(contact, wd)
        # save changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

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
        # home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # work phone
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        # secondary phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                first_name = element.find_element_by_xpath("td[3]").text
                last_name = element.find_element_by_xpath("td[2]").text
                address = element.find_element_by_xpath("td[4]").text
                all_phones = element.find_element_by_xpath("td[6]").text
                all_emails = element.find_element_by_xpath("td[5]").text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id,address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_xpath("td")[8]
        cell.find_element_by_xpath("//img[@alt='Edit']").click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        #email_2 = wd.find_element_by_name("email2").get_attribute("value")
        #email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, first_name=first_name, last_name=last_name, address=address, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone,
                       email=email)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)




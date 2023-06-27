#задание 7
class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("Number of results")) > 0):
            wd.find_element_by_link_text("home page").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("New group")) > 0):
            wd.find_element_by_link_text("group page").click()
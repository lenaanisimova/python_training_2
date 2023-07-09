#задание 13
from sys import maxsize

class Contact:
    def __init__(self, id=None, first_name=None, last_name=None, address=None,
                 mobile_phone=None, home_phone=None, work_phone=None, secondary_phone=None, all_phones_from_home_page=None,
                 email=None, email_2=None, email_3=None, all_emails_from_home_page=None,
                 day_of_birth=None, month_of_birth=None, year_of_birth=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
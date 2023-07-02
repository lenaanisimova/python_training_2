#задание 13
from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last_name=None, address=None, mobile_phone=None, email=None, day_of_birth=None, month_of_birth=None,
                        year_of_birth=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile_phone = mobile_phone
        self.email = email
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
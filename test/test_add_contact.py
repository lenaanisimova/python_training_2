#задание 7
import pytest
from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
def random_digits(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
def random_ascii_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
def random_email(maxlen_1, maxlen_2, maxlen_3):
    prefix = string.ascii_letters + string.digits + "-" + "." + "_"
    domen = string.ascii_lowercase
    email = "".join([random.choice(prefix) for i in range(random.randrange(maxlen_1))]) + "@" + \
            "".join([random.choice(domen) for i in range(random.randrange(maxlen_2))]) + "." +\
            "".join([random.choice(domen) for i in range(random.randrange(maxlen_3))])
    return email
def random_dbirth():
    day = random.randint(1, 28)
    return str(day)
def random_dmonth():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])
def random_dyear():
    year = random.randint(1900, 2022)
    return str(year)
testdata = [
    Contact(first_name=random_ascii_letters("first_name", 10), last_name=random_ascii_letters("last_name", 10),
            address=random_string("address", 15), mobile_phone=random_digits(11), home_phone=random_digits(15),
            work_phone=random_digits(15), secondary_phone=random_digits(15), email=random_email(10, 5, 3),
            day_of_birth=random_dbirth(), month_of_birth=random_dmonth(), year_of_birth=random_dyear())
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    #app.session.login(login="admin", password="secret")
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


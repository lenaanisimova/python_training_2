#задание 19
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
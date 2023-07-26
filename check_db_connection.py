#задание 20

#import mysql.connector
import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group


#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    #l = db.get_contacts_in_group(Group(id="11"))
    #from item in l:
    #     print(item)
    # print(len(l))

    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()
import os
import re

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="labris",
    user='sunman',
    password='labris')

cur = conn.cursor()

"""
cur.execute('Select * from users;')
results = cur.fetchall()
print(results)
"""

cur.execute(f"Select password from users where username =  'sunman' ")
results = cur.fetchall()

password = results[0][0]

cur.execute(f"Select username from users ")
results = cur.fetchall()

for i in results: print(i[0])
conn.commit()

username = 'user13'

cur.execute(f"Select * from users where username =  '{username}' ")
results = cur.fetchall()
print(results)




"""
email = 'adsg@asd.com'
password = 'Password54'
mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
password_regex = re.compile(r'[A-Za-z0-9@#$%^&+=.]{8,}')

if re.fullmatch(mail_regex, email):
    print('mail match')

if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print('password match ')
"""
import sqlite3

conn = sqlite3.connect('mydatabase.db')

sql = 'CREATE TABLE movies (link TEXT, image_link TEXT, name VARCHAR, rate VARCHAR)'
cursor = conn.cursor()

cursor.execute(sql)
conn.close()
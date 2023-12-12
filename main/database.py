import sqlite3

conn = sqlite3.connect('mydatabase.db')

sql = 'CREATE TABLE movies (link TEXT, image_link TEXT, name VARCHAR, rate VARCHAR)'
sql = 'SELECT * FROM movies'
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()

# for r in res:
    # print("Name:", r[2])

conn.close()
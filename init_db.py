import sqlite3

connection = sqlite3.connect('data/db/database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Charts', 'Automated Strategy Analysis Coming Soon')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Options?', 'A new set of tools designed to help calculate all of the math required to trade options at a very profitable level.')
            )

connection.commit()
connection.close()
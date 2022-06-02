# pull the data from the SQLight 
# This just to make me learn Fadhel do that 

import sqlite3

con = sqlite3.connect('/Users/benabdi/Desktop/FlS/flaskblog/site.db')

# Create a SQL connection to our SQLite database

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM post;'):
    print(row)

# Be sure to close the connection
con.close()


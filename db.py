import sqlite3

con = sqlite3.connect("TTX.db")
cur = con.cursor()
#cur.execute("CREATE TABLE chat(id text, user text, comment text, time datetime)")
#cur.execute("drop table chat")
cur.execute("DELETE FROM chat")
#cur.execute("CREATE TABLE incident(id text, json text)")
#cur.execute("SELECT * FROM chat")
#for row in cur:
#    print(row)
con.commit()
con.close()
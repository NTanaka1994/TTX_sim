import sqlite3

con = sqlite3.connect("TTX.db")
cur = con.cursor()
#cur.execute("CREATE TABLE chat(id text, user text, comment text, time datetime)")
#cur.execute("drop table chat")
cur.execute("DELETE FROM chat")
con.commit()
con.close()
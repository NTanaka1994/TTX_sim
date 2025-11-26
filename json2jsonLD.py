import json
import sqlite3

f = open("cards.json", "r", encoding="utf-8")
jsn = f.read()

dic = json.loads(jsn)
#print(dic["attacks"])
atk = dic["attacks"]
dst = []
for i in range(len(atk)):
    dic = {}
    context = {"name" : "http://schema.org/name",
               "description": "http://schema.org/description",
               "identifier": "http://schema.org/identifier",
               "tag": "http://schema.org/keywords",
               "severity": "https://w3id.org/security#severity",
               "SecurityThreat": "https://w3id.org/security#SecurityThreat"
               }
    dic["@context"] = context
    dic["@type"] = "SecurityThreat"
    dic["identifier"] = atk[i]["id"]
    dic["name"] = atk[i]["title"]
    dic["description"] = atk[i]["description"]
    dic["tag"] = atk[i]["tags"]
    dic["severity"] = atk[i]["baseScore"]
    con = sqlite3.connect("TTX.db")
    cur = con.cursor()
    cur.execute("INSERT INTO incident (id, json) values (?, ?)", (str(i), json.dumps(dic)))
    con.commit()
    con.close()
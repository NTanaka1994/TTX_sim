import json

f = open("cards.json", "r", encoding="utf-8")
jsn = f.read()
f.close()
dic = json.loads(jsn)
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
    dst.append(dic)
f = open("jsonld.json", "w", encoding="utf-8")
f.write(json.dumps(dst))
f.close()
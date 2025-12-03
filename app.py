from flask import Flask, redirect, render_template, session, url_for, request
from flask_socketio import SocketIO, emit, join_room
from datetime import timedelta
from datetime import datetime
from openai import OpenAI
import sqlite3
import html
import json

app = Flask("__name__")
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)
app.permanent_session_lifetime = timedelta(minutes=1800)
f = open("API_key.txt", "r", encoding="utf-8")
key = f.read()

@app.route("/")
def route():
    return redirect("home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/discussion/<incident_num>/<role>")
def discussion(incident_num, role):
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    if incident_num not in session:
        session[incident_num] = now_str
    res = ""
    con = sqlite3.connect("TTX.db")
    cur = con.cursor()
    cur.execute("SELECT user, comment FROM chat WHERE id=? AND time>?",(incident_num,session[incident_num]))
    for user, text in cur:
        res += html.escape(user) + ": " + html.escape(text) + "<br>"
    con.close()
    con = sqlite3.connect("TTX.db")
    jsn = ""
    cur = con.cursor()
    cur.execute("SELECT json FROM incident WHERE id=?", (incident_num,))
    for row in cur:
        jsn = row[0]
    dic = json.loads(jsn)
    con.close()
    return render_template("discussion.html", incident_num=incident_num, incident=html.escape(dic["name"]), des=html.escape(dic["description"]), role=html.escape(role), chat=res)

@app.route("/judge/<incident_num>", methods=["POST"])
def judge(incident_num):
    result = request.form["result"]
    chat = ""
    con = sqlite3.connect("TTX.db")
    cur = con.cursor()
    cur.execute("SELECT time, user, comment FROM chat WHERE id=?",(incident_num,))
    chat += "会話記録\n"
    for time, user, comment in cur:
        chat += "時刻 : " + html.escape(str(time)) + "\t" +html.escape(user) + " \t: " + html.escape(comment) + "\n"
    res = chat + "\n" + "対応 : " + html.escape(result)
    con.close()
    con = sqlite3.connect("TTX.db")
    jsn = ""
    cur = con.cursor()
    cur.execute("SELECT json FROM incident WHERE id=?", (incident_num,))
    for row in cur:
        jsn = row[0]
    dic2 = json.loads(jsn)
    con.close()
    client = OpenAI(api_key=key)
    prompt = f"""
    あなたはサイバー攻撃対処の専門家です。
    次のインシデント対応とその過程の議事録について100点満点で採点してください。
    
    # インシデント内容
    {dic2['name']}
    
    # 採点基準
    1. 技術的妥当性(40点)
    2. 組織的対応と迅速性(30点)
    3. 被害抑止への貢献度(30点)
    
    # チーム内での会話議事録
    {chat}
    
    # 最終回答
    {result}
    
    出力形式は次のJSONとしてください。
    {{
        "score" : 数値,
        "reason" : "理由の説明",
        "advice" : "改善点"
    }}
    """
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
    mes = response.choices[0].message.content
    try:
        dic = json.loads(mes)
    except:
        mes = mes.replace("```json", "")
        mes = mes.replace("\n```", "")
        print(mes)
        dic = json.loads(mes)
        
    res = "<h2>点数</h2>" + str(dic["score"]) + "点\n<h2>理由</h2>" + html.escape(dic["reason"]).replace("。", "。\n") + "\n<h2>アドバイス</h2>\n" + html.escape(dic["advice"]).replace("。", "。\n") + "\n以下議事録と最終決定" + res
    con = sqlite3.connect("TTX.db")
    cur = con.cursor()
    cur.execute("DELETE FROM chat WHERE id=?",(incident_num,))
    con.commit()
    con.close()
    return render_template("judge.html", res=res, incident=html.escape(dic2["name"]), des=html.escape(dic2["description"]))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@socketio.on("join")
def on_join(data):
    room = data["room"]
    join_room(room)
    emit("chat", {"msg" : f"{ data['user']} joined" }, room=room)

@socketio.on("message")
def on_message(data):
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    con = sqlite3.connect("TTX.db")
    cur = con.cursor()
    cur.execute("INSERT INTO chat (id, user, comment, time) values (?, ?, ?, ?)",(data["room"], data["user"], data["msg"], now_str))
    con.commit()
    con.close()
    emit("chat", {"msg" : f"{data['user']}: {data['msg']}"}, room=data["room"])

if __name__ == "__main__":
    socketio.run(app, port=80, host="0.0.0.0", allow_unsafe_werkzeug=True)
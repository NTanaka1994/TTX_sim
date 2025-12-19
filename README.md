# TTX_sim
## 使用方法
<pre>
このリポジトリをクローンしてください。
「API_key.txt」を作りOpenAIからAPIキーを取得してAPI_key.txtに保存してください。
  app.pyを起動して下さい。
使用するライブラリはFlask、Flask-socketio、OpenAI、SQLite3
データベーステーブルは
chat
id, comment, time

incident
id, json(JSON-LD形式)
</pre>

## 演習選択画面
<pre>
  最初の人は名前を入力してランダム演習を押下してください。そしてチャットに何らかの文字を入力してください。
  二番目以降の人は最初に入った人のインシデント番号を教えてもらってから番号を確認してインシデント番号と名前を入力してボタンを押下し演習画面に入ってください。
</pre>
<img width="905" height="511" alt="image" src="https://github.com/user-attachments/assets/717789c9-0fe7-4065-9075-542bf4d72c8d" />

## 演習画面
<pre>
  あなたはCSIRTの一員として発生したインシデントを確認(h1タグのタイトル)しチャットで議論してください。
  そしてチャットで議論し終え、最終的な動きを共有でき次第、チャットに入っている誰か一人が画面一番下のテキストボックスを入力してボタンを押してください。
  万が一遷移先で500エラーが出たらAlt＋←で前に戻ってもう一回送信してください。
</pre>
<img width="1400" height="684" alt="image" src="https://github.com/user-attachments/assets/403d67f8-b4f5-45ea-b1de-7fcf0be2d5f2" />

## REDTEAM
AIがレッドチームを担当します
<img width="1400" height="694" alt="image" src="https://github.com/user-attachments/assets/e79fc91b-6cf0-4e5d-8d6e-190a5ca4b90a" />



## 最終的な採点はこんな感じ
<pre>
　レポートが出力されます。採点はOpenAIのGPT-4o-miniを使っています。
</pre>
<img width="1400" height="602" alt="image" src="https://github.com/user-attachments/assets/dc5f87cc-8270-4db5-964b-10fb1b01a930" />


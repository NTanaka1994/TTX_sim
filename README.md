# TTX_sim
## 使用方法
<pre>
このリポジトリをクローンしてください。
「API_key.txt」を作りOpenAIからAPIキーを取得してAPI_key.txtに保存してください。
  app_ver2.pyを起動して下さい。
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
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/01c9058f-e03d-466d-9af6-f7bb5d00b45f" />

## 最終的な採点はこんな感じ
<pre>
　レポートが出力されます。採点はOpenAIのGPT-4o-miniを使っています。
</pre>
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/3d96c5fa-2d35-4cbf-94a1-67bf2ff8e675" />

※英語版作ってくれる人、お願いします！(当方英語めちゃくちゃ苦手)

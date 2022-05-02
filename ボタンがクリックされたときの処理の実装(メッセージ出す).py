import tkinter
from tkinter import messagebox

# click時のイベント
#bit_click関数の実行でタイトル[メッセージ]の[こんにちは]というメッセージのメッセージボックスが出る
def btn_click():
    messagebox.showinfo("メッセージ", "こんにちは")
def btn2_click():
    messagebox.showinfo("メッセージ", "Hello")
def btn3_click():
    z = 1+ 1
    messagebox.showinfo("メッセージ", z)


# 画面作成
#画面作成するためのTk関数利用
#変数 = tkinter.Tk()
tki = tkinter.Tk()
tki.geometry('300x200') # 画面サイズの設定(横×縦),ここでの×は小文字のx(エックス)
tki.title('ボタンがクリックされた時の処理を見よう') # 画面タイトルの設定

# ボタンの作成
#ボタンがクリックされたときbtn_click関数が実行されるようになっている(command= 呼び出したい関数)
#背景色が色コード#f0e68cの色になっている(bg=背景色にしたい色のコード)
#文字職が色コード#ff0000の色担っている(fg=文字色にしたい色のコード)
#ボタンの横幅･ｻｲｽﾞはwidth=横幅･ｻｲｽﾞ
btn = tkinter.Button(tki, text='こんにちは', command = btn_click, bg='#f0e68c',fg='#ff0000',width=20)
btn2 = tkinter.Button(tki, text='Hello', command = btn2_click, bg='#f0e68c',fg='#ff0000',width=20)
btn3 = tkinter.Button(tki, text='1+1は?', command = btn3_click, bg='#f0e68c',fg='#ff0000',width=20)
#xの数字が大きいほど右へ位置する,yの数字が大きくなるほど下へ位置する
btn.place(x=80, y=80) #ボタンを配置する位置の設定
btn2.place(x=80, y=110)
btn3.place(x=80,y=150)
# 画面をそのまま表示
tki.mainloop()

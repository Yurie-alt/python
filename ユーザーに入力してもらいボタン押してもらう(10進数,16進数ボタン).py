import tkinter


#click時のイベントを関数で作る
def btn_click():
    # テキスト取得
    #変数 = int(テキストボックスが格納された変数)
    num = int(txt_1.get())
    # 16進数へ変換してテキストボックスへセット
    txt_2.insert(0, hex(num)) 



#画面作成
tki = tkinter.Tk()

tki.geometry('400x300')#ここでの×は小文字のx(エックス)
tki.title('ユーザーに入力してもらう')

# ラベル
#変数 = tkinter.Label(ラベルとしてtext=表示させたい文字)
lbl_1 = tkinter.Label(text='10進数')
lbl_1.place(x=120, y=120)#変数に格納したラベルの位置設定
lbl_2 = tkinter.Label(text='16進数')
lbl_2.place(x=120, y=150)

# テキストボックス
#変数=tkinter.Entry(width=テキストボックスのｻｲｽﾞ)
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=170, y=120)#テキストボックスの位置指定
txt_2 = tkinter.Entry(width=20)
txt_2.place(x=170, y=150)

# ボタン
btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=160, y=250)


#画面そのまま表示
tki.mainloop()

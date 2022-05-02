import tkinter
from tkinter import messagebox#messageboxモジュールをインポート


string = "5"

tki = tkinter.Tk()
tki.geometry('300x200')


def btn_click():
    #テキストボックスを格納した変数.get()でテキストボックスの文字を取得
    messagebox.showinfo("出力結果", txt.get())

def clear_click():
    #変数txtに格納したテキストボックスの中身を削除
    txt.delete(0,tkinter.END)

def input_btn_click():
    #引数に指定した文字列をテキストボックスに入力(下では変数stringに入った文字列)
    txt.insert(tkinter.END,string)

#ボタン作成
#command=ボタンが押されたら実行される関数
btn = tkinter.Button(tki, text='出力', command=btn_click)
btn.place(x= 110,y=100)

#クリアボタン作成
clear = tkinter.Button(tki, text='クリア', command= clear_click)
clear.place(x=150,y=100)

#インプットボタン作成
input_btn = tkinter.Button(tki, text='5', command=input_btn_click)
input_btn.place(x=90,y=100)
#テキストボックス作成
txt = tkinter.Entry(width=20)
txt.place(x=70,y=70)

tki.mainloop()

import tkinter

def clear_click():
    #変数txtに格納したテキストボックスの中身を削除
    txt.delete(0,tkinter.END)

#1をクリックした時
def btn1_click():
    txt.insert(tkinter.END,"1")
#2をクリックした時
def btn2_click():
    txt.insert(tkinter.END,"2")
#3をクリックした時
def btn3_click():
    txt.insert(tkinter.END,"3")
#4をクリックした時
def btn4_click():
    txt.insert(tkinter.END,"4")
def btn5_click():
    txt.insert(tkinter.END,"5")
def btn6_click():
    txt.insert(tkinter.END,"6")
def btn7_click():
    txt.insert(tkinter.END,"7")
def btn8_click():
    txt.insert(tkinter.END,"8")
def btn9_click():
    txt.insert(tkinter.END,"9")
def plusbtn_click():
    txt.insert(tkinter.END,"+")
def equalbtn_click():
    txt.insert(tkinter.END,"=" + str(eval(txt.get())))
def mulbtn_click():
    txt.insert(tkinter.END,"*")
def minusbtn_click():
    txt.insert(tkinter.END,"-")
def dividebtn_click():
    txt.insert(tkinter.END,"/")
def pointbtn_click():
    txt.insert(tkinter.END,".")


tki = tkinter.Tk()
tki.geometry('300x200')
tki.title("ボタン")



#x
a= 90
b= a + 35
c= b + 35
#y
d = 60
e = d + 25
f = e + 25

#テキストボックス作成
txt = tkinter.Entry(width=23)
txt.place(x=90,y=40)



#クリアボタン作成
clear = tkinter.Button(tki, text='C', command= clear_click,width=3)
clear.place(x=a,y=f+25)
#=ボタン作成
clear = tkinter.Button(tki, text='=', command= equalbtn_click,width=3)
clear.place(x=c,y=f+25)

#+
plusbtn = tkinter.Button(tki,text="+",command=plusbtn_click,width=3)
plusbtn.place(x=c+33,y=f+25)
#-
plusbtn = tkinter.Button(tki,text="-",command=minusbtn_click,width=3)
plusbtn.place(x=c+33,y=f)
#x
mulbtn = tkinter.Button(tki,text="x",command=mulbtn_click,width=3)
mulbtn.place(x=c+33,y=d)
#÷
dividebtn = tkinter.Button(tki,text="÷",command=dividebtn_click,width=3)
dividebtn.place(x=c+33,y=e)
#.
pointbtn = tkinter.Button(tki,text=".",command=pointbtn_click,width=3)
pointbtn.place(x=b,y=f+25)


#1
btn1 = tkinter.Button(tki,text="1",command=btn1_click,width=3)
btn1.place(x=a,y=f)
#2
btn2 = tkinter.Button(tki,text="2",command=btn2_click,width=3)
btn2.place(x=b,y=f)
#3
btn3 = tkinter.Button(tki,text="3",command=btn3_click,width=3)
btn3.place(x=c,y=f)
#4
btn4 = tkinter.Button(tki,text="4",command=btn4_click,width=3)
btn4.place(x=a,y=e)
#5
btn5 = tkinter.Button(tki,text="5",command=btn5_click,width=3)
btn5.place(x=b,y=e)
#6
btn6 = tkinter.Button(tki,text="6",command=btn6_click,width=3)
btn6.place(x=c,y=e)
#7
btn7 = tkinter.Button(tki,text="7",command=btn7_click,width=3)
tki.title("ボタン")
btn7.place(x=a,y=d)
#8
btn8 = tkinter.Button(tki,text="8",command=btn8_click,width=3)
tki.title("ボタン")
btn8.place(x=b,y=d)
#9
btn9 = tkinter.Button(tki,text="9",command=btn9_click,width=3)
btn9.place(x=c,y=d)







tki.mainloop()

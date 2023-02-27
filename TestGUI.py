from tkinter import *
from tkinter import ttk #Theme of tk
from tkinter import messagebox

#หน้าจอหลักโปรแกรม
GUI = Tk()
GUI.title('กีฬาที่ชื่นชอบ')
GUI.geometry('600x400')

L1 = Label(GUI,text='กีฬาที่ชื่นชอบ',font=('Angsana New',24),fg='orange')
L1.place(x=230,y=20)
##################

def Button1():
    text = 'บาสเก็ตบอล'
    messagebox.showinfo('ท่านชอบเล่นกีฬา',text)
    
FB1 = Frame(GUI)
FB1.place(x=250,y=80)
B1 = ttk.Button(FB1,text='บาสเกตบอล',command=Button1)
B1.pack(ipadx=10,ipady=10,expand=YES)

##################

def Button2():
    text = 'ว่ายน้ำ'
    messagebox.showinfo('ท่านชอบเล่นกีฬา',text)
    
FB2 = Frame(GUI)
FB2.place(x=250,y=140)
B2 = ttk.Button(FB2,text='ว่ายน้ำ',command=Button2)
B2.pack(ipadx=10,ipady=10,expand=YES)

##################

def Button3():
    text = 'แบดมินตัน'
    messagebox.showinfo('ท่านชอบเล่นกีฬา',text)
    
FB3 = Frame(GUI)
FB3.place(x=250,y=200)
B3 = ttk.Button(FB3,text='แบดมินตัน',command=Button3)
B3.pack(ipadx=10,ipady=10,expand=YES)

GUI.mainloop()

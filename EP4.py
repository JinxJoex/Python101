from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
#############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกและจัดเก็บข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('400x300') #นี่คือขนาดโปรแกรม

D1 = ttk.LabelFrame(GUI,text='ป้อนข้อมูล')
D1.place(x=100,y=50)

ShwData = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
A1 = ttk.Entry(D1,textvariable=ShwData,font=('Cordia New',16))
A1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = ShwData.get() #ดึงข้อมูลจากตัวแปร ShwData มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    ShwData.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B1 = ttk.Button(D1,text='บันทึก',command=SaveData)
B1.pack(ipadx=10,ipady=10)


D2 = ttk.LabelFrame(GUI,text='ข้อมูล')
D2.place(x=150,y=200)

def ReadData():
    
    datacsv = readcsv()
    messagebox.showinfo('อ่านข้อมูลในไฟล์',datacsv)

B2 = ttk.Button(D2,text='อ่านข้อมูล',command=ReadData)
B2.pack(ipadx=10,ipady=10)


GUI.mainloop()

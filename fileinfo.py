# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:25:15 2019

@author: qiansihan
"""
from tkinter import *
import tkinter.messagebox as mes
import tkinter.simpledialog as sim
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Simhei']
import webbrowser

root=Tk()
root.geometry('750x560')
root.title('文本编辑器')
mes.showinfo('Welcome','欢迎使用文本编辑器!')
Label(root,text='欢迎使用文本编辑器',fg='blue',font=50).place(x=300,y=30)
Label(root,text='文本输入',fg='green',font=30).place(x=10,y=80)
text1=Text(root,bd=3,fg='red')
text1.place(x=110,y=80)

filetext=open('english.txt','r')
lines=list(filetext.readlines())
line0=''.join(lines)
text1.insert(INSERT,line0)
wenben0=text1.get('1.0',INSERT)

textb=Text(root,width=80,height=2)
textb.insert(INSERT,"点击打开163邮件服务器首页(不信你试试( iwi ))--------------------")
textb.tag_add('link','1.2','1.12')
textb.tag_config('link',foreground='green',underline=True,background='pink')
def show_hand_cursor(event):
    textb.config(cursor='arrow')
def click(event):
    webbrowser.open('https://mail.163.com/')
def show_arrow_cursor(event):
    textb.config(cursor='xterm')
textb.tag_bind('link','<Enter>',show_hand_cursor)
textb.tag_bind('link','<Button-1>',click)
textb.tag_bind('link','<Leave>',show_arrow_cursor)
textb.place(x=110,y=460)

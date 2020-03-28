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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:35:52 2018

@author: pangshan
"""

import tkinter as tk


if __name__ == '__main__':
    window=tk.Tk()
    window.title('SW600 Final project')
    window.geometry('1000x1000')
    window.resizable(width=True,height=True)
    
tk.Label(window,text='Basketball Game Predictor',font=('Arial',20),bg='CORNFLOWERBLUE',
         width=100,height=3).pack()
frm = tk.Frame(window)
frm.pack()

frm_t = tk.Frame(frm)
frm_b = tk.Frame(frm)

frm_t.pack(side='top')
frm_b.pack(side='bottom')

l1=tk.Label(frm_t,text='Data',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=0,column=0)
l2=tk.Label(frm_t,text='Home Team',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=1,column=0)
l3=tk.Label(frm_t,text='Away Team',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=2,column=0)
l4=tk.Label(frm_t,text='Balance',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=0,column=2)
l5=tk.Label(frm_t,text='Mkt Odds',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=1,column=2)
l6=tk.Label(frm_t,text='My Odds',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=2,column=2)
l7=tk.Label(frm_t,text='Bet Amount',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=0,column=4)
e1 = tk.StringVar()
e2 = tk.StringVar()
e3 = tk.StringVar()
e4 = tk.StringVar()
e5 = tk.StringVar()
e6 = tk.StringVar()
entry1=tk.Entry(frm_t,textvariable = e1).grid(row=0,column=1)
entry2=tk.Entry(frm_t,textvariable = e2).grid(row=1,column=1)
entry3=tk.Entry(frm_t,textvariable = e3).grid(row=2,column=1)
entry4=tk.Entry(frm_t,textvariable = e4).grid(row=0,column=3)
entry5=tk.Entry(frm_t,textvariable = e5).grid(row=1,column=3)
entry6=tk.Entry(frm_t,textvariable = e6).grid(row=2,column=3)
v=tk.StringVar()
r1=tk.Radiobutton(frm_t, text='Bet H',variable=v).grid(row=1,column=4)
r2=tk.Radiobutton(frm_t,text='Bet A',variable=v).grid(row=2,column=4)

b=tk.Button(frm_b,text='Bet',fg='red',font=('Arial',18),
            width=10,command=bet_result).pack(side='top')     
t = tk.Text(frm_b,width=50,height=20)
t.pack(fill=tk.X, expand=1)



tk.mainloop()
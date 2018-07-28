#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:35:52 2018

@author: pangshan
"""

import tkinter as tk
from tkinter import ttk

def bet_home():
    """
    1. set team based on v

    2. use team name and date select team from dataframe


    :return:
    """
    return
    # try:
    #     if v.get() == 1:
    #         team = home_team.get()
    #     elif v.get() == 2:
    #         team = away_team.get()
    #     print team
    # except tk.TclError:
    #     return


def bet_away():
    """
    1. set team based on v

    2. use team name and date select team from dataframe


    :return:
    """
    return
    # try:
    #     if v.get() == 1:
    #         team = home_team.get()
    #     elif v.get() == 2:
    #         team = away_team.get()
    #     print team
    # except tk.TclError:
    #     return

def reset():
    value_list = [date, home_team, away_team, balance, mkt_odds, my_odds, bet_amount]
    for value in value_list:
        value.set('')

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

#所有label

label_date=tk.Label(frm_t,text='Data',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=0,column=0)
label_home_team=tk.Label(frm_t,text='Home Team',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=1,column=0)
label_away_team=tk.Label(frm_t,text='Away Team',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=2,column=0)
label_balance=tk.Label(frm_t,text='Balance',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=0,column=2)
label_mkt_odds=tk.Label(frm_t,text='Mkt Odds',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=1,column=2)
label_my_odds=tk.Label(frm_t,text='My Odds',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=2,column=2)
label_bet_amount=tk.Label(frm_t,text='Bet Amount',fg='white',bg='black',font=('Arial',18),
            width=10).grid(row=0,column=4)
date = tk.StringVar()
balance = tk.StringVar()
mkt_odds = tk.StringVar()
my_odds = tk.StringVar()
bet_amount = tk.StringVar()

#所需要的输入部分
txt_date=tk.Entry(frm_t, textvariable=date).grid(row=0,column=1, sticky=tk.W)
txt_balance=tk.Entry(frm_t, textvariable=balance).grid(row=0,column=3, sticky=tk.W)
txt_mkt_odds=tk.Entry(frm_t, textvariable=mkt_odds).grid(row=0,column=5, sticky=tk.W)
txt_my_odds=tk.Entry(frm_t, textvariable=my_odds).grid(row=1,column=3, sticky=tk.W)
txt_bet_amount=tk.Entry(frm_t, textvariable=bet_amount).grid(row=2,column=3, sticky=tk.W)

#所需要的下拉列表
home_team= tk.StringVar()
home_team_chosen=ttk.Combobox(frm_t,textvariable=home_team)
home_team_chosen['values']=('a','b','c','d')
home_team_chosen['state'] = "readonly"
home_team_chosen.grid(row=1,column=1, sticky=tk.W)

away_team=tk.StringVar()
away_team_chosen=ttk.Combobox(frm_t,textvariable=away_team)
away_team_chosen['values']=('a','b','c','d')
away_team_chosen['state'] = "readonly"
away_team_chosen.grid(row=2,column=1, sticky=tk.W)

#bet的按钮

btn_home_team=tk.Button(frm_t, text='Bet Home',width=15,height=2, command=bet_home).grid(row=1,column=4,columnspan=2, sticky=tk.W)
btn_away_team=tk.Button(frm_t,text='Bet Away',width=15,height=2, command=bet_away).grid(row=2,column=4,columnspan=2, sticky=tk.W)

btn_reset = tk.Button(frm_t, text='Reset', font=('Arial', 18), command=reset).grid(row=1, column=5, sticky=tk.W)

bet_display= tk.Text(frm_b,width=50,height=20)
bet_display.pack(fill=tk.X, expand=1)

tk.mainloop()
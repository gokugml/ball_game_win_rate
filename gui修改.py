#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:35:52 2018

@author: pangshan
"""

import tkinter as tk
from tkinter import ttk
#import ball_game


if __name__ == '__main__':
    window=tk.Tk()
    window.title('SW600 Final project')
    window.geometry('1000x1000')
    window.resizable(width=True,height=True)

def bet():
    """
    1. set team based on v

    2. use team name and date select team from dataframe


    :return:
    """
    try:
        if v.get() == 1:
            team = home_team.get()
        elif v.get() == 2:
            team = away_team.get()
        print team
    except tk.TclError:
        return

def reset():
    value_list = [date, home_team, away_team, balance, mkt_odds, my_odds, bet_amount]
    for value in value_list:
        value.set('')

tk.Label(window, text='Basketball Game Predictor', font=('Arial', 20), bg='CORNFLOWERBLUE',
         width=100, height=3).pack()
frm = tk.Frame(window)
frm.pack()

frm_t = tk.Frame(frm)
frm_b = tk.Frame(frm)

frm_t.pack(side='top')
frm_b.pack(side='bottom')

label_date = tk.Label(frm_t, text='Date', fg='white', bg='black', font=('Arial', 18),
                      width=10).grid(row=0, column=0)
label_home_team = tk.Label(frm_t, text='Home Team', fg='white', bg='black', font=('Arial', 18),
                           width=10).grid(row=1, column=0)
label_away_team = tk.Label(frm_t, text='Away Team', fg='white', bg='black', font=('Arial', 18),
                           width=10).grid(row=2, column=0)
label_balance = tk.Label(frm_t, text='Balance', fg='white', bg='black', font=('Arial', 18),
                         width=10).grid(row=0, column=2)
label_mkt_odds = tk.Label(frm_t, text='Market Odds', fg='white', bg='black', font=('Arial', 18),
                          width=10).grid(row=1, column=2)
label_my_odds = tk.Label(frm_t, text='My Odds', fg='white', bg='black', font=('Arial', 18),
                         width=10).grid(row=2, column=2)
label_bet_amount = tk.Label(frm_t, text='Bet Amount', fg='white', bg='black', font=('Arial', 18),
                            width=10).grid(row=0, column=4)
#这些变量是否需要？
date = tk.StringVar()
home_team = tk.StringVar()
away_team = tk.StringVar()
balance = tk.StringVar()
balance = tk.StringVar()
mkt_odds = tk.StringVar()
my_odds = tk.StringVar()
bet_amount = tk.StringVar()
#输入各项内容
txt_date = tk.Entry(frm_t, textvariable=date).grid(row=0, column=1, sticky=tk.W)
txt_balance = tk.Entry(frm_t, textvariable=balance).grid(row=0, column=3, sticky=tk.W)
txt_mkt_odds = tk.Entry(frm_t, textvariable=mkt_odds).grid(row=1, column=3, sticky=tk.W)
txt_my_odds = tk.Entry(frm_t, textvariable=my_odds).grid(row=2, column=3, sticky=tk.W)
txt_bet_amount = tk.Entry(frm_t, textvariable=bet_amount).grid(row=0, column=5, sticky=tk.W)

#设置主队客队下拉列表
home_team=('a','b','c','d')
homeTeam= tk.StringVar(value=home_team)
away_team=('a','b','c','d')
awayTeam=tk.StringVar(value=away_team)
home_team_chosen=ttk.Combobox(frm_t,textvariable=home_team).grid(row=2,column=0)
away_team_chosen=ttk.Combobox(frm_t,textvariable=away_team).grid(row=2,column=1)

#设置两个button
v = tk.IntVar()
btn_home_team=tk.Button(frm_t, text='Bet H',width=15,
                        height=2).grid(row=1,column=4,columnspan=2)
butn_away_team=tk.Button(frm_t,text='Bet A',width=15,
                        height=2).grid(row=2,column=4,columnspan=2)


#设置输出
bet_display = tk.Text(frm_b, width=50, height=20)
bet_display.pack(fill=tk.X, expand=1)

tk.mainloop()


















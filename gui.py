#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:35:52 2018

@author: pangshan, Menglong, Yandong
"""

import tkinter as tk
from tkinter import ttk
import win_rate
import os

# my data
work_dir = os.getcwd()
my_data = win_rate.Data(work_dir)
r_work_dir = "/".join(work_dir.split('\\'))
my_bet = win_rate.Bet(r_work_dir)


# GUI
def bet_home():
    date = date_chosen.get()
    my_balance = txt_balance.get()
    bet_amount = txt_bet_amount.get()
    market_odds = txt_market_odds.get()
    home = home_team_chosen.get()
    my_game_result = my_data.get_result(home=home, date=date)
    my_profit, new_balance = my_bet.bet_result(balance=my_balance, bet_amount=bet_amount, market_odds=market_odds,
                                               game_result=my_game_result)
    if my_game_result == "W":
        game_result.set("Win")
    elif my_game_result == "L":
        game_result.set("Loss")
    profit.set(my_profit)
    balance.set(new_balance)
    return


def skip_game():
    date = date_chosen.get()
    home = home_team_chosen.get()
    my_game_result = my_data.get_result(home=home, date=date)
    if my_game_result == "W":
        game_result.set("Win")
        profit.set("Miss a win bet!")
    elif my_game_result == "L":
        game_result.set("Loss")
        profit.set("Wisdom skip!")


def get_win_ratio():
    date = date_chosen.get()
    home = home_team_chosen.get()
    away = away_team_chosen.get()
    ratio = my_bet.get_win_ratio(date=date, home=home, away=away)
    win_ratio.set(ratio)
    market_odds = txt_market_odds.get()
    EV, bet = my_bet.bet_or_not(win_ratio_h=ratio, market_odds=market_odds)
    ev.set(EV)
    if bet == False:
        bet_or_not.set("Do NOT Bet!")
    elif bet == True:
        bet_or_not.set("Bet!")
    return


def reset():
    value_list = [date, home_team, away_team, balance, mkt_odds, bet_amount]
    for value in value_list:
        value.set('')


window = tk.Tk()
window.title('SW600 Final project')
window.geometry('1000x1000')
window.resizable(width=True, height=True)

tk.Label(window, text='Basketball Game Predictor', font=('Arial', 20), bg='CORNFLOWERBLUE',
         width=100, height=3).pack()
frm = tk.Frame(window)
frm.pack()

frm_t = tk.Frame(frm)
frm_b = tk.Frame(frm)

frm_t.pack(side='top')
frm_b.pack(side='bottom')

# 所有label

label_date = tk.Label(frm_t, text='Data', fg='white', bg='black', font=('Arial', 18),
                      width=10).grid(row=0, column=0)
label_home_team = tk.Label(frm_t, text='Home Team', fg='white', bg='black', font=('Arial', 18),
                           width=10).grid(row=1, column=0)
label_away_team = tk.Label(frm_t, text='Away Team', fg='white', bg='black', font=('Arial', 18),
                           width=10).grid(row=2, column=0)
label_balance = tk.Label(frm_t, text='Balance', fg='white', bg='black', font=('Arial', 18),
                         width=10).grid(row=0, column=2)
label_mkt_odds = tk.Label(frm_t, text='Market Odds', fg='white', bg='black', font=('Arial', 18),
                          width=10).grid(row=1, column=2)
# label_my_odds=tk.Label(frm_t,text='My Odds',fg='white',bg='black',font=('Arial',18),
#             width=10).grid(row=2,column=2)
label_bet_amount = tk.Label(frm_t, text='Bet Amount', fg='white', bg='black', font=('Arial', 18),
                            width=10).grid(row=2, column=2)
label_ev = tk.Label(frm_t, text='EV', fg='white', bg='black', font=('Arial', 18),
                    width=10).grid(row=1, column=4)
label_bet_or_not = tk.Label(frm_t, text='Bet or Not', fg='white', bg='black', font=('Arial', 18),
                            width=10).grid(row=2, column=4)
label_game_result = tk.Label(frm_b, text='Game Result', fg='white', bg='CORNFLOWERBLUE', font=('Arial', 18),
                             width=10).grid(row=0, column=3)
label_profit = tk.Label(frm_b, text='Profit', fg='white', bg='CORNFLOWERBLUE', font=('Arial', 18),
                        width=10).grid(row=0, column=5)
balance = tk.StringVar()
mkt_odds = tk.StringVar()
# my_odds = tk.StringVar()
bet_amount = tk.StringVar()
win_ratio = tk.StringVar()
bet_or_not = tk.StringVar()
ev = tk.StringVar()
game_result = tk.StringVar()
profit = tk.StringVar()

# 所需要的输入部分
txt_balance = tk.Entry(frm_t, textvariable=balance)
txt_balance.grid(row=0, column=3, sticky=tk.W)
txt_market_odds = tk.Entry(frm_t, textvariable=mkt_odds)
txt_market_odds.grid(row=1, column=3, sticky=tk.W)
# txt_my_odds=tk.Entry(frm_t, textvariable=my_odds)
# txt_my_odds.grid(row=2,column=3, sticky=tk.W)
txt_bet_amount = tk.Entry(frm_t, textvariable=bet_amount)
txt_bet_amount.grid(row=2, column=3, sticky=tk.W)
txt_win_ratio = tk.Entry(frm_t, textvariable=win_ratio)
txt_win_ratio.grid(row=0, column=5, sticky=tk.W)
txt_ev = tk.Entry(frm_t, textvariable=ev)
txt_ev.grid(row=1, column=5, sticky=tk.W)
txt_bet_or_not = tk.Entry(frm_t, textvariable=bet_or_not)
txt_bet_or_not.grid(row=2, column=5, sticky=tk.W)
txt_game_result = tk.Entry(frm_b, textvariable=game_result)
txt_game_result.grid(row=0, column=4, sticky=tk.W)
txt_profit = tk.Entry(frm_b, textvariable=profit)
txt_profit.grid(row=0, column=6, sticky=tk.W)

# 所需要的下拉列表
date = tk.StringVar()
date_chosen = ttk.Combobox(frm_t, textvariable=date)
date_chosen['values'] = my_data.get_date_list('TOR')  # TODO: use home team and away team date
date_chosen['state'] = "readonly"
date_chosen.grid(row=0, column=1, sticky=tk.W)

home_team = tk.StringVar()
home_team_chosen = ttk.Combobox(frm_t, textvariable=home_team)
home_team_chosen['values'] = ['TOR']
home_team_chosen['state'] = "readonly"
home_team_chosen.grid(row=1, column=1, sticky=tk.W)

away_team = tk.StringVar()
away_team_chosen = ttk.Combobox(frm_t, textvariable=away_team)
away_team_chosen['values'] = ['IND']
away_team_chosen['state'] = "readonly"
away_team_chosen.grid(row=2, column=1, sticky=tk.W)

# bet的按钮

btn_get_win_ratio = tk.Button(frm_t, text='Home win ratio', width=20, height=1, command=get_win_ratio).grid(row=0,
                                                                                                            column=4,
                                                                                                            sticky=tk.W)

btn_home_team = tk.Button(frm_b, text='Bet Home', width=15, height=2, command=bet_home).grid(row=0, column=1,
                                                                                             sticky=tk.W)
btn_skip_game = tk.Button(frm_b, text='Skip Game', width=15, height=2, command=skip_game).grid(row=0, column=2,
                                                                                               sticky=tk.W)
# btn_reset = tk.Button(frm_t, text='Reset', font=('Arial', 18), command=reset).grid(row=2, column=5, sticky=tk.W)
#
# bet_display= tk.Text(frm_b,width=50,height=20)
# bet_display.pack(side='bottom', fill=tk.X, expand=1)

tk.mainloop()

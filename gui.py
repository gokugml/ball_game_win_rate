#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:35:52 2018

@author: pangshan
"""

import tkinter as tk
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
date = tk.StringVar()
home_team = tk.StringVar()
away_team = tk.StringVar()
balance = tk.StringVar()
balance = tk.StringVar()
mkt_odds = tk.StringVar()
my_odds = tk.StringVar()
bet_amount = tk.StringVar()

txt_date = tk.Entry(frm_t, textvariable=date).grid(row=0, column=1, sticky=tk.W)
txt_home_team = tk.Entry(frm_t, textvariable=home_team).grid(row=1, column=1, sticky=tk.W)
txt_away_team = tk.Entry(frm_t, textvariable=away_team).grid(row=2, column=1, sticky=tk.W)
txt_balance = tk.Entry(frm_t, textvariable=balance).grid(row=0, column=3, sticky=tk.W)
txt_mkt_odds = tk.Entry(frm_t, textvariable=mkt_odds).grid(row=1, column=3, sticky=tk.W)
txt_my_odds = tk.Entry(frm_t, textvariable=my_odds).grid(row=2, column=3, sticky=tk.W)
txt_bet_amount = tk.Entry(frm_t, textvariable=bet_amount).grid(row=0, column=5, sticky=tk.W)

v = tk.IntVar()
r1 = tk.Radiobutton(frm_t, text='Bet Home', variable=v, value=1, indicatoron=0).grid(row=1, column=4)
r2 = tk.Radiobutton(frm_t, text='Bet Away', variable=v, value=2, indicatoron=0).grid(row=2, column=4)

b = tk.Button(frm_b, text='Bet', fg='red', font=('Arial', 18),
              width=10, command=bet).pack(side='top')
t = tk.Text(frm_b, width=50, height=20)
t.pack(fill=tk.X, expand=1)

tk.mainloop()

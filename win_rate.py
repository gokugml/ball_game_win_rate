import os
import rpy2.robjects as robjects
import pandas


class Data(object):
    def __init__(self, workdir=os.getcwd()):
        self._workdir = os.path.abspath(workdir)

    def clean_table(self):
        return

    def get_date_list(self, home):
        home = os.path.join(self._workdir, home + ".csv")
        date_list = []
        df = pandas.read_csv(home)
        for item in df['Date']:
            date = item.split('-')
            date_list.append("{}/{}/{}".format(date[1], date[2], date[0]))
        return date_list

    def get_result(self, home, date):
        home = os.path.join(self._workdir, home + ".csv")
        df = pandas.read_csv(home)
        temp = date.split('/')
        date = "{}-{}-{}".format(temp[2], temp[0], temp[1])
        for i in range(len(df)):
            # print df.ix[i]
            if df.ix[i]['Date'] == date:
                return df.ix[i]['W/L']
            else:
                continue
        print("Home {} do not have game on {}".format(home, date))
        return -1


class Bet(object):
    def __init__(self, workdir=os.getcwd()):
        robjects.r(r'''setwd("{}")'''.format(workdir))

    def get_win_ratio(self, date, home, away):
        home = home + ".csv"
        away = away + ".csv"
        robjects.r.source('engine.r')
        win_ratio = robjects.r.simulation(date, home, away)
        return win_ratio[0]

    def bet_result(self, balance, bet_amount, market_odds, game_result):
        balance = float(balance)
        bet_amount = float(bet_amount)
        market_odds = float(market_odds)
        if game_result == 'W':
            profit = bet_amount * market_odds
        else:
            profit = -bet_amount
        balance = balance + profit
        return profit, balance

    def bet_or_not(self, win_ratio_h, market_odds):
        key = False
        win_ratio_h = float(win_ratio_h)
        market_odds = float(market_odds)
        EV = win_ratio_h * market_odds - (1 - win_ratio_h)
        if EV > 0.05:
            key = True
        return EV, key


if __name__ == '__main__':
    test_data = Data()
    test_data.get_date_list('TOR')
    print test_data.get_result('TOR', '11/24/2017')
    # test = Bet(workdir="\"C:/Users/Menglong/python/basketball_game_predictor-master/\"")
    # test.get_win_ratio('12/1/2017', 'TOR.csv', 'IND.csv')

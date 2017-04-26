import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta



def get_stock_data(ticker):
	end_date = date.today()
	start_date = end_date - timedelta(days=14)
	stock = web.DataReader(ticker,'yahoo', start_date, end_date)
	print(stock)
	stock['Percent'] = (stock['Adj Close']-stock['Adj Close'].shift(1))/stock['Adj Close']*100
	pct_change = stock['Percent'].tolist()
	change_list=[]
	for i in pct_change:
		short = '%.2f' % i
		change_list.append(short)
	change_list[0] = '0'
	name = [ticker]
	final_list = name+change_list
	dates = stock.index.values
	date_list = ['Date']
	for day in dates:
		correct = str(day)[:10]
		date_list.append(correct)
	stock_dict = {'stock': final_list, 'date_list': date_list}
	return stock_dict

print(get_stock_data('NFLX'))




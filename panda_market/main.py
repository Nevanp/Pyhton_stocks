# Nevan Parsley NRP211 11274655
# Dr. Jeffery Long


import math as m
import numpy as np
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as mp

userInput = input('Input stock idea you would like to view: ').upper()

print('The YTD closing data as of', datetime.datetime.today(),'is:')

stock_data = pdr.get_data_yahoo(userInput,
                          start=datetime.datetime(datetime.datetime.today().year, 1, 1),
                          end=datetime.datetime.today())

# print(stock_data) # shows the format of 
stock = np.array(stock_data)
stk = stock[0:, -1].flatten()
norm_stk = []
norm_stk = np.convolve(stk, [1, -1])

## stock price YTD
mp.plot(stk)
mp.title('YTD value')
mp.xlabel(userInput)
mp.show()
#stock change YTD
mp.plot(norm_stk[1:-1])
mp.title('YTD change per day')
mp.xlabel(userInput)
mp.show()
print("Max increase in close,", max(norm_stk[1:]), "Max Decrease in close,", min(norm_stk[:-1]))
print('Average change in closing price', sum(norm_stk[1:-1])/(len(norm_stk)-2))
if sum(norm_stk[1:-1]) > 0:
    print("The stock value has INCREASED", sum(norm_stk[1:-1]), "so far this year")
else:
    print("The stock value has DECREASED", sum(norm_stk[1:-1]), "so far this year")

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:24:01 2019

@author: jose
"""

prices = [400, 450, 465, 525, 650, 700]
prices.append(675)
#prices.append([675, 100])
print(prices) # append add one more element to the list

new_prices = [750, 790, 890, 975, 1195, 1200]

all_prices = prices + new_prices # add new_prices to the end of prices, create new result list
prices.extend(new_prices) # append all items of new_prices to prices 
# extend joins two different lists
print(len(prices))
"""
for each_price in prices:
    print('The price was ' + str(each_price))

print('>>>')
# We use range on the length of prices to make sure we go through all list indices.
for index in range(len(prices)):
    price = prices[index]
    print('The price was ' + str(price))
"""    
for index in range(len(prices)-1): #why do we have this -1 here? why does it crash?
    if prices[index + 1]> prices[index]:
        print('Prices went up at index ' + str(index))
    else:
        print('Prices went down at index ' + str(index))
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 06:55:07 2023

@author: admin
"""

import pandas as pd

data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')
data.info()
var = ('apple', 'pear','banana')
var = {'name': 'Doo', 'Location':'Saouth Africa'}

var = True

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6


ProfitPerItem = 21.11 - 11.73
ProfitPerItem = 21.11 * 11.73
ProfitPerItem = 21.11 / 11.73

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased + ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem

SellingPricePerTransaction = NumberofItemsPurchased + SellingPricePerItem

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberofItemsPurchased

data['CostPerTransaction'] = CostPerTransaction

#another way of multiplying


data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']



#SalesPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


#profit

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup

data['markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']


#round

roundmarkup = round(data['markup'],2)

data['markup'] = roundmarkup

#combining date

date = day + '-' + data['Month'] + '-' + year
print(date)
data['Date'] = date


#change type

day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)

#using iloc

data.iloc[0]  
data.iloc[0:3]  
data.head(5)
data.iloc[4,2]

#clientkeywords

split_col = data['ClientKeywords'].str.split(',',expand =True)


data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]


#replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthofContract'] = data['ClientAge'].str.replace(']','')


#lowercase

data['ItemDescription'] = data['ItemDescription'].str.title()


#merging a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on='Month')

#dropping columns

data = data.drop('ClientKeywords', axis = 1)

data.to_csv('ValueInc_Cleaned.csv', index = False)














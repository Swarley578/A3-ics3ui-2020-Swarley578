# Quinn A3Q1 code
# Reading a csv file
# import panda to do the math
import pandas as pd
# code to find and read your csv file
df = pd.read_csv (r'C:\Users\Quinn\PycharmProjects\ICSCSV.csv')

# code to create the averages of each column
# this code finds all the numbers under each column and finds the average
mean1 = df['Total Cases'].mean()
mean2 = df['New Cases'].mean()
mean3 = df['Total Deaths'].mean()
mean4 = df['Total Recovered'].mean()
mean5 = df['Active Cases'].mean()
mean6 = df['Serious, Critical'].mean()
mean7 = df['Tot Cases/1M pop'].mean()
mean8 = df['Deaths/1M pop'].mean()
mean9 = df['Total Tests'].mean()
mean10 = df['Tests/1M pop'].mean()

# code to find max and min value for each column
# this code finds all the numbers under each column and finds the maximum and minimum values
max1 = df['Total Cases' 'Country'].max()
min1 = df['Total Cases' 'Country'].min()
max2 = df['Total Deaths' 'Country'].max()
min2 = df['Total Deaths' 'Country'].min()
max3 = df['Total Deaths' 'Country'].max()
min3 = df['Total Deaths' 'Country'].min()
max4 = df['Total Recovered' 'Country'].max()
min4 = df['Total Recovered' 'Country'].min()
max5 = df['Active Cases' 'Country'].max()
min5 = df['Active Cases' 'Country'].min()
max6 = df['Serious, Critical' 'Country'].max()
min6 = df['Serious, Critical' 'Country'].min()
max7 = df['Tot Cases/1M pop' 'Country'].max()
min7 = df['Tot Cases/1M pop' 'Country'].min()
max8 = df['Deaths/1M pop' 'Country'].max()
min8 = df['Deaths/1M pop' 'Country'].min()
max9 = df['Total Tests' 'Country'].max()
min9 = df['Total Tests' 'Country'].min()
max10 = df['Tests/1M pop' 'Country'].max()
min10 = df['Tests/1M pop' 'Country'].min()

# code to print average values
# the + str adds the math for the averages to print the value of the averages
print ('Average number of cases:' + str(mean1))
print ('Average number of new cases:' + str(mean2))
print ('Average number of deaths:' + str(mean3))
print ('Average number of recovered:' + str(mean4))
print ('Average number of active cases:' + str(mean5))
print ('Average number of serious/critical cases:' + str(mean6))
print ('Average number of cases/1M:' + str(mean7))
print ('Average number of deaths/1M:' + str(mean8))
print ('Average number of tests:' + str(mean9))
print ('Average number of tests/1M:' + str(mean10))

# code to print max and min values
print ('Max cases:' + str(max1))
print ('Min cases:' + str(min1))
print ('Max new cases:' + str(max2))
print ('Min new cases:' + str(min2))
print ('Max number of deaths:' + str(max3))
print ('Min number of deaths:' + str(min3))
print ('Max number of active cases:' + str(max4))
print ('Min number of active cases:' + str(min4))
print ('Max number of active cases:' + str(max5))
print ('Min number of active cases:' + str(min5))
print ('Max number of serious/critical cases:' + str(max6))
print ('Min number of serious/critical cases:' + str(min6))
print ('Max number of cases/1M:' + str(max7))
print ('Min number of cases/1M:' + str(min7))
print ('Max number of deaths/1M:' + str(max8))
print ('Min number of deaths/1M:' + str(min8))
print ('Max number of tests:' + str(max9))
print ('Min number of tests:' + str(min9))
print ('Max number of tests/1M:' + str(max10))
print ('Min number of tests/1M:' + str(max10))
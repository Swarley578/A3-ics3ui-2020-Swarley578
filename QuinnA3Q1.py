# code for Quinn A3Q1
# code to import pandas so you are able to do math
import pandas as pd
# code to find and read your csv file
# use the path file to find where it is stored and then use the file name
data = pd.read_csv (r'C:\Users\Quinn\PycharmProjects\ICS.csv')

# code to get rid of all comas so that the program can do the math
data['Total Cases'] = data['Total Cases'].apply(lambda x: float(x.split()[0].replace(',', '')))
data['New Cases'] = data['New Cases'].apply(lambda x: float(x.split()[0].replace(',', '')))
data['Total\r\nDeaths'] = data['Total\r\nDeaths'].apply(lambda x: float(x.split()[0].replace(',', '')))
data['Total\r\nRecovered'] = data['Total\r\nRecovered'].apply(lambda x: float(x.split()[0].replace(',', '')))
data['Active\r\nCases'] = data['Active\r\nCases'].apply(lambda x: float(x.split()[0].replace(',', '')))
data['Tot Cases/\r\n1M pop'] = data['Tot Cases/\r\n1M pop'].apply(lambda x: float(x.split()[0].replace(',', '')))
data['Total\r\nTests'] = data['Total\r\nTests'].apply(lambda x: float(x.split()[0].replace(',', '')))


# code to find the averages of numbers in each column
mean1 = data['Total Cases'].mean()
mean2 = data['New Cases'].mean()
mean3 = data['Total\r\nDeaths'].mean()
mean4 = data['Total\r\nRecovered'].mean()
mean5 = data['Active\r\nCases'].mean()
mean6 = data['Tot Cases/\r\n1M pop'].mean()
mean7 = data['Total\r\nTests'].mean()
mean8 = data['New\r\nDeaths'].mean()

# code to find maximum and minimum values
max1 = data['Total Cases'].max()
min1 = data['Total Cases'].min()
max2 = data['New Cases'].max()
min2 = data['New Cases'].min()
max3 = data['Total\r\nDeaths'].max()
min3 = data['Total\r\nDeaths'].min()
max4 = data['Total\r\nRecovered'].max()
min4 = data['Total\r\nRecovered'].min()
max5 = data['Active\r\nCases'].max()
min5 = data['Active\r\nCases'].min()
max6 = data['Tot Cases/\r\n1M pop'].max()
min6 = data['Tot Cases/\r\n1M pop'].min()
max7 = data['Total\r\nTests'].max()
min7 = data['Total\r\nTests'].min()
max8 = data['New\r\nDeaths'].max()
min8 = data['New\r\nDeaths'].min()

# code to print the average value
print ("Important data for Corona Virus")
print ("Average of Total Cases: " + str(mean1))
print ("Average number of new cases: " + str(mean2))
print ('Average number of deaths:' + str(mean3))
print ('Average number of recovered:' + str(mean4))
print ('Average number of active cases:' + str(mean5))
print ('Average number of cases/1M:' + str(mean6))
print ('Average number of tests:' + str(mean7))
print ('Average number of new deaths:' + str(mean8))

# code to Print Max and Min Values
print ('Max cases:' + str(max1))
print ('Min cases:' + str(min1))
print ('Max new cases:' + str(max2))
print ('Min new cases:' + str(min2))
print ('Max number of deaths:' + str(max3))
print ('Min number of deaths:' + str(min3))
print ('Max number of recovered:' + str(max4))
print ('Min number of recovered:' + str(min4))
print ('Max number of active cases:' + str(max5))
print ('Min number of active cases:' + str(min5))
print ('Max number of cases/1M:' + str(max6))
print ('Min number of cases/1M:' + str(min6))
print ('Max number of tests:' + str(max7))
print ('Min number of tests:' + str(min7))
print ('Max number of new deaths' + str(max8))
print ('Min number of new deaths' + str(min8))

# code to print whole table
# code to display all rows and columns
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)
minValuesObj = data.max()
# code to print data sheet if word table is typed
x = input("Type in table to see full data sheet")
print (data)

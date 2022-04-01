#%%
#### Reading and Writing files

# Read
f = open('sample.txt', mode='r')
contents_read = f.read()
f.close()

print(contents_read)

#%%
# Write
myName = 'Pragith'
someSentence = 'I am a boy'

f = open('new_file_to_write.txt', mode='w')
f.write('My name is: ' + myName + '\n')
f.write(someSentence)
f.close()


#%%
# Append
import random

someRandomNum = random.random()

x = open('new_file_to_write.txt', mode='a')
#x.write('\nI am appending a new sentence')
#x.write('\nA random number is: ' + someRandomNum)
for i in range(1,10):
    someRandomInt = random.randint(5,20)
    x.write('\nThe ' + str(i) + ' random number is: ' + str(someRandomInt))
x.close()


#%%
# Binary
y = open('einstein.jpg', 'rb')
imageContents = y.read()
y.close()

z = open('newEinstein.jpg', 'wb')
z.write(imageContents)
z.close()

#%%
#### APIs

###### Single From and To Currency Converter ######
import requests

# User variables
forexAmount = 35
fromCurrency = 'USD'
toCurrency = 'INR'


# Program variables
API_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={fromCurrency}&to_currency={toCurrency}&apikey=6H7O7NFYFOROM4V3'


# Make the API call
responseObj = requests.get(API_URL)

# Understand the API response
#print(responseObj.headers)
#print(responseObj.status_code)
#print(responseObj.text)

# Extract data from the API response
responseData = responseObj.json()
forexRate = float(responseData['Realtime Currency Exchange Rate']['5. Exchange Rate'])

# Calculate the converted forex amount
convertedAmount = forexAmount * forexRate

print(f'{fromCurrency} {forexAmount} = {toCurrency} {convertedAmount}')

##############################################################


#%%
###### Single From and Multiple To Currency Converter ########
import requests

# User variables
forexAmount = 35
fromCurrency = 'USD'
toCurrencies = ['CAD', 'INR', 'EUR', 'GBP']

for toCurrency in toCurrencies:
    # Program variables
    API_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={fromCurrency}&to_currency={toCurrency}&apikey=6H7O7NFYFOROM4V3'

    # Make the API call
    responseObj = requests.get(API_URL)

    # Extract data from the API response
    responseData = responseObj.json()
    forexRate = float(responseData['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    # Calculate the converted forex amount
    convertedAmount = forexAmount * forexRate

    print(f'{fromCurrency} {forexAmount} = {toCurrency} {convertedAmount}')

##############################################################

#%%
#### Dataframes
import pandas as pd

namesDF = pd.read_excel('excel_data.xlsx')

# Exploring the dataframe
print(namesDF)
print(namesDF.iloc[0])
print(namesDF['name'])


namesDF['check_fav_number'] = namesDF['fav_number'].apply(lambda x: 'Even' if x%2==0 else 'Odd')
namesDF


#%%
## Tuples vs Lists
# Tuples - They are immutable lists
a = (1,2,3)
b = [1,2,3]
c = [4,5,6]
d = (4,5,6)

## Lambda functions
add_num = lambda n1,n2: n1+n2
hello_the_message = lambda name,msg: f'Hello, {name}! {msg}'

print(add_num(45,60))
print(hello_the_message('Janani','It is a wonderful day!'))

# %%

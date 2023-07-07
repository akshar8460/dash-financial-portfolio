import csv
import random

# Define the list of stock symbols
stock_symbols = ['BNS', 'T.TO', 'PLTR', 'SHOP.P']

# Generate random data for 200 rows
rows = []
for _ in range(200):
    stock_symbol = random.choice(stock_symbols)
    quantity = random.randint(1, 100)
    purchase_price = round(random.uniform(10, 100), 2)
    rows.append([stock_symbol, quantity, purchase_price])

# Write the data to the CSV file
with open('portfolio.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Stock Symbol', 'Quantity', 'Purchase Price'])
    writer.writerows(rows)

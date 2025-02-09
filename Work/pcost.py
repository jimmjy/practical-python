# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(fileName):
    shares = 'shares'
    price = 'price\n'
    
    try:
        with open(fileName, 'rt') as file:
            price_index = None
            shares_index = None
            total_cost = 0
            
            # this moves the cursor to the second line after this statement, so
            # the for loop will start after the headers
            headers = next(file).split(',')
            
            try:
                price_index = headers.index(price)
                shares_index = headers.index(shares)
            except Exception as error:
                print(error)
            

            for line in file:
                line_list = line.split(',')

                shares_in_line = int(line_list[shares_index])
                price_in_line = float(line_list[price_index])
                total_cost += price_in_line * shares_in_line
            
            return total_cost
    except Exception as error:
        print(error.args[1])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)

print(f"Total cost: {cost}")

    
"""
    A better way to process csv files is to use csv library
    
    import csv
    
    f = open(fileLocation)
    rows = csv.reader(f) // here we pass f to csv.reader
    next(rows) // this has a pointer at top of file, this reads first line
    
"""
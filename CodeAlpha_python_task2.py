# TASK 2: Stock Portfolio Tracker 
# ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock prices. 
# ● Simplified Scope: 
# ○ User inputs stock names and quantity. 
# ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}). 
# ○ Display total investment value and optionally save the result in a .txt or .csv file. 
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional). 

# Hardcoded stock prices for some example companies
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2700, "AMZN": 3300, "MSFT": 300}

# Dictionary to store user's portfolio (stock symbol -> quantity)
portfolio = {}


# Function to print available stocks and their prices
def print_available_stocks():
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")


# Welcome message and show available stocks
print("Welcome to the Stock Portfolio Tracker!")
print_available_stocks()

# Main input loop: user enters stock symbols and quantities
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    # Check if the stock symbol is valid
    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        if qty < 0:
            print("Quantity cannot be negative.")
            continue
    except ValueError:
        print("Please enter a valid integer for quantity.")
        continue
    # Add or update the stock in the portfolio
    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty


# Calculate and display total investment
print("\nYour Portfolio:")
total = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"  {stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
    total += value
print(f"Total Investment Value: ${total}")

# Optionally save the portfolio to a file
save = input("Do you want to save your portfolio to a file? (y/n): ").lower()
if save == "y":
    filename = input("Enter filename (e.g., portfolio.txt): ")
    with open(filename, "w") as f:
        # Write header
        f.write("Stock,Quantity,Price,Value\n")
        # Write each stock's data
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
        # Write total investment
        f.write(f"Total Investment Value,,,{total}\n")
    print(f"Portfolio saved to {filename}")
else:
    print("Portfolio not saved.")

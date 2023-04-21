import yfinance as yf
import json

# Define the initial account balance
account_balance = 10000.0

# Define the portfolio
portfolio = {}

# Load the portfolio from a file if it exists
filename = "portfolio.json"
try:
    with open(filename, "r") as f:
        portfolio = json.load(f)
except FileNotFoundError:
    pass

# Buy stocks
ticker = input("Enter the ticker symbol: ")
shares = int(input("Enter the number of shares: "))
stock_data = yf.Ticker(ticker).info
current_price = stock_data['regularMarketOpen']
cost = shares * current_price
if cost > account_balance:
    print("Not enough funds.")
else:
    account_balance -= cost
    if ticker in portfolio:
        portfolio[ticker]["shares"] += shares
        portfolio[ticker]["price"] = current_price
    else:
        portfolio[ticker] = {"shares": shares, "price": current_price}

# Sell stocks
ticker = input("Enter the ticker symbol: ")
shares = int(input("Enter the number of shares: "))
stock_data = yf.Ticker(ticker).info
current_price = stock_data['regularMarketOpen']
proceeds = shares * current_price
if ticker not in portfolio or shares > portfolio[ticker]["shares"]:
    print("Invalid transaction.")
else:
    account_balance += proceeds
    portfolio[ticker]["shares"] -= shares

# Save the portfolio to a file
with open(filename, "w") as f:
    json.dump(portfolio, f)

# Print the portfolio
print("Current Portfolio:")
for ticker, data in portfolio.items():
    shares = data["shares"]
    price = data["price"]
    value = shares * price
    print(f"{ticker}: {shares} shares at {price:.2f} per share, worth {value:.2f}")
print(f"Account balance: {account_balance:.2f}")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total = 0

print(" Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or type done): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock] * quantity
        total += investment

        print("Investment value:", investment)

    else:
        print(" Stock not found!")

print("\ Total Investment:", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: {total}")

print(" Data saved in portfolio.txt")
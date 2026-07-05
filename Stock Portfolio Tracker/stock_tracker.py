# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

print("=" * 45)
print("📈 STOCK PORTFOLIO TRACKER")
print("=" * 45)

# User input
stock_name = input("Enter Stock Name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

if stock_name in stock_prices:

    quantity = int(input("Enter Quantity: "))

    price = stock_prices[stock_name]

    total = price * quantity

    print("\n========== RESULT ==========")
    print("Stock :", stock_name)
    print("Price :", price)
    print("Quantity :", quantity)
    print("Total Investment : $", total)

    # Save to file
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("----------------------\n")
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Price: ${price}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: ${total}\n")

    print("\n✅ Report saved as portfolio.txt")

else:
    print("❌ Invalid Stock Name!")

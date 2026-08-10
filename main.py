# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print(f"{quantity} shares of {stock} added.")
    print(f"Investment: ${investment}")


# Display portfolio
print("\n===== Your Portfolio =====")

for item in portfolio:
    print(
        f"{item['stock']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ${item['price']} | "
        f"Value: ${item['investment']}"
    )

print(f"\nTotal Investment: ${total_investment}")


# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("===== Stock Portfolio =====\n\n")

    for item in portfolio:
        file.write(
            f"{item['stock']} | "
            f"Quantity: {item['quantity']} | "
            f"Price: ${item['price']} | "
            f"Value: ${item['investment']}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved to portfolio.txt")
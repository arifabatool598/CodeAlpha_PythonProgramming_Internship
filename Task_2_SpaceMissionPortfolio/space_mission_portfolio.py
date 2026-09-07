# Space Mission Investment Tracker

import csv

# Manually defined example prices for space-related assets.
# These are fictional values for this programming task.
space_assets = {
    "SPACEX": 250,
    "ROCKETLAB": 85,
    "ASTROSAT": 120,
    "LUNAR-X": 150,
    "MARS-X": 200
}

portfolio = {}
total_investment = 0

print("===== Space Mission Investment Tracker =====")
print("Available assets:", ", ".join(space_assets.keys()))

while True:
    asset = input("\nEnter asset name (or type 'done' to finish): ").upper()

    if asset == "DONE":
        break

    if asset not in space_assets:
        print("Asset not found. Please choose from the available assets.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {asset}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        value = space_assets[asset] * quantity

        portfolio[asset] = portfolio.get(asset, 0) + quantity
        total_investment += value

        print(
            f"{asset}: {quantity} units x "
            f"${space_assets[asset]} = ${value}"
        )

    except ValueError:
        print("Please enter a valid whole number.")

print("\n===== Space Portfolio Summary =====")

for asset, quantity in portfolio.items():
    value = space_assets[asset] * quantity
    print(f"{asset}: {quantity} units = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional CSV output
with open("space_portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Asset", "Quantity", "Price", "Investment"])

    for asset, quantity in portfolio.items():
        value = space_assets[asset] * quantity
        writer.writerow([asset, quantity, space_assets[asset], value])

    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total_investment])

print("\nSummary saved to space_portfolio_summary.csv")
"""
Phase 1 of Calder Pizza Company
"""
__author__ = "298496 Ayaan Shahzad"
__version__ = "0.0.1"
__license__ = "MIT"
# Variables
branch = "Calder Pizza Company."
print("Hello and Welcome to", branch)
total = 0
price_small = 5.50
price_medium = 7.90
price_large = 12.00
price_topping = 0.75
available_toppings = [
    "Pepperoni", "Mushroom", "Extra cheese", "Sausage",
    "Onion", "Black olives", "Green pepper", "Fresh garlic",
    "Tomato", "Fresh basil"
]
small_orders = []
medium_orders = []
large_orders = []

# Code.
while True:

# Ask for pizza size.
    while True:
        size = input("What size pizza do you want? (small, medium, large): ").lower()
        if size in ["small", "medium", "large"]:
            break
        print("Please enter small, medium or large.")

    if size == "small":
        price = price_small
    elif size == "medium":
        price = price_medium
    else:
        price = price_large

# Ask for number of toppings.
    while True:
        toppings_count = input("How many toppings do you want? (0–3): ")
        if toppings_count.isdigit():
            toppings_count = int(toppings_count)
            if 0 <= toppings_count <= 3:
                break
        print("Enter a number between 0 and 3.")

# Choose toppings.
    toppings = []

    if toppings_count > 0:
        print("\nAvailable toppings:")
        for i in range(len(available_toppings)):
            print(f"{i + 1}. {available_toppings[i]}")

        for i in range(toppings_count):
            while True:
                choice = input(f"Choose topping {i + 1}: ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(available_toppings):
                        toppings.append(available_toppings[choice - 1])
                        break
                print("Invalid choice.")

# Calculate cost of pizza.
    pizza_cost = price + (toppings_count * price_topping)
    total += pizza_cost

# Storing the order.
    order = {
        "size": size,
        "toppings": toppings,
        "cost": pizza_cost
    }
    if size == "small":
        small_orders.append(order)
    elif size == "medium":
        medium_orders.append(order)
    else:
        large_orders.append(order)

# Output order details.
    print("\nYour Order")
    print("Size:", size)
    print("Toppings:", ", ".join(toppings) if toppings else "None")
    print(f"Pizza cost: £{pizza_cost:.2f}")
    print(f"Total so far: £{total:.2f}")
    print()

# Ask to continue.
    again = input("Do you want to order another pizza? (y/n): ").lower()
    if again != "y":
        break

# Final order summary
print("\nFinal Order Summary")
print("Small pizzas:", len(small_orders))
print("Medium pizzas:", len(medium_orders))
print("Large pizzas:", len(large_orders))
print(f"Grand Total: £{total:.2f}")
print("Thank you for your order!")

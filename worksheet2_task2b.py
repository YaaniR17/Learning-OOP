"""
Phase 1 of Calder Pizza Company.
"""
__author__ = "298496 Ayaan Shahzad"
__version__ = "0.0.1"
__license__ = "MIT"
# Classes.
class Menu:
    def __init__(self):
        self.price_small = 5.50
        self.price_medium = 7.90
        self.price_large = 12.00
        self.price_per_topping = 0.75

        self.available_toppings = [
            "Pepperoni", "Mushroom", "Extra cheese", "Sausage",
            "Onion", "Black olives", "Green pepper", "Fresh garlic",
            "Tomato", "Fresh basil"
        ]

    def get_price(self, size):
        if size == "small":
            return self.price_small
        elif size == "medium":
            return self.price_medium
        else:
            return self.price_large

class Pizza:
    def __init__(self, size, toppings, cost):
        self.size = size
        self.toppings = toppings
        self.cost = cost

class Order:
    def __init__(self):
        self.small = []
        self.medium = []
        self.large = []
        self.total = 0

    def add_pizza(self, pizza):
        if pizza.size == "small":
            self.small.append(pizza)
        elif pizza.size == "medium":
            self.medium.append(pizza)
        else:
            self.large.append(pizza)

        self.total += pizza.cost

    def show_summary(self):
        print("\nFinal Order Summary")
        print("Small pizzas ordered:", len(self.small))
        print("Medium pizzas ordered:", len(self.medium))
        print("Large pizzas ordered:", len(self.large))
        print(f"Grand Total: £{self.total:.2f}")
        print("Thank you for your order!")
        print()

class PizzaShop:
    def __init__(self):
        self.branch = "Calder Pizza Company."
        self.menu = Menu()
        self.order = Order()

    def display_welcome_message(self):
        print(f"Hello and Welcome to {self.branch}")

    def ask_size(self):
        size = input("What size pizza do you want? (small, medium, large): ").lower()
        if size in ["small", "medium", "large"]:
            return size
        print("Not valid. Please enter small, medium or large.")
        return self.ask_size()

    def ask_topping_count(self):
        num = input("How many toppings do you want? A maximum of 3 please: ")
        if num.isdigit():
            num = int(num)
            if 0 <= num <= 3:
                return num
        print("Enter a number from 0 to 3 please.")
        return self.ask_topping_count()

    def ask_single_topping(self, num):
        choice = input(f"Topping {num}: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(self.menu.available_toppings):
                return self.menu.available_toppings[choice - 1]
        print("Invalid choice.")
        return self.ask_single_topping(num)

    def choose_toppings(self, count):
        toppings = []

        if count > 0:
            print("\nAvailable toppings:")
            for i in range(len(self.menu.available_toppings)):
                print(f"{i + 1}. {self.menu.available_toppings[i]}", end="   ")
            print("\n")

            for i in range(1, count + 1):
                toppings.append(self.ask_single_topping(i))

        return toppings

    def display_pizza(self, pizza):
        print("\nYour Order Details")
        print("Size:", pizza.size.capitalize())
        print("Toppings:", ", ".join(pizza.toppings) if pizza.toppings else "None")
        print(f"Pizza cost: £{pizza.cost:.2f}")
        print(f"Total: £{self.order.total:.2f}")
        print()

    def get_pizza_order(self):
        size = self.ask_size()
        topping_count = self.ask_topping_count()
        toppings = self.choose_toppings(topping_count)

        base_price = self.menu.get_price(size)
        cost = base_price + topping_count * self.menu.price_per_topping

        pizza = Pizza(size, toppings, cost)
        self.order.add_pizza(pizza)
        self.display_pizza(pizza)

    def ask_to_continue(self):
        while True:
            answer = input("Do you want to restart? (y/n): ").lower()
            if answer == "y":
                print("\nProgram restarting...\n")
                return True
            elif answer == "n":
                print("\nProgram has ended. Goodbye!\n")
                return False
            else:
                print("Not valid.")

    def start(self):
        self.display_welcome_message()
        print()
        self.get_pizza_order()
        self.order.show_summary()


class Program:
    def run(self):
        shop = PizzaShop()
        while True:
            shop.start()
            if not shop.ask_to_continue():
                break
# Code.
Program().run()

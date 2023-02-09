from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


items = [MenuItem("latte", 200, 150, 24, 3.0),
         MenuItem("espresso", 50, 0, 24, 1.5),
         MenuItem("cappuccino", 250, 100, 24, 3.0)]

menu = Menu()
options = menu.get_items()
coffee = CoffeeMaker()
money = MoneyMachine()


while True:
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        break
    for item in items:
        if choice == "report":
            coffee.report()
            money.report()
            break
        elif choice == item.name and coffee.is_resource_sufficient(item):
            payment = money.make_payment(item.cost)
            if payment:
                coffee.make_coffee(item)

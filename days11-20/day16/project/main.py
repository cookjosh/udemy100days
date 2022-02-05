import resource
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_items = menu.get_items()

machine_on = True
while machine_on == True:
    user_input = input(f"What would you like? ({menu_items}): ").lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        machine_on = False
    elif user_input == "latte" or "espresso" or "cappuccino":
        user_order = menu.find_drink(user_input)
        cost = user_order.cost
        print(f"{user_input} costs ${cost}0.")
        if coffee_maker.is_resource_sufficient(user_order) == True:
            payment_check = money_machine.make_payment(cost)
            if payment_check == True:
                coffee_maker.make_coffee(user_order)

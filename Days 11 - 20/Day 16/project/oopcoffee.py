from menu import Menu, MenuItem
from machine import CoffeeMaker
from money import MoneyMachine

men_methd = Menu()
cmnd_methd = CoffeeMaker()
money_methd = MoneyMachine()

is_on = True

while is_on:
    choices = men_methd.get_items()
    cmnd = input(f"What would you like? {choices} : ").lower()
    if cmnd == 'off':
        print('Successfully Turned off, Run the Program to Begin Again')
        is_on = False
    elif cmnd == 'report':
        cmnd_methd.report()
        money_methd.report()
    else:
        drink = men_methd.find_drink(cmnd)
        
        if cmnd_methd.is_resource_sufficient(drink) and money_methd.make_payment(drink.cost):
            cmnd_methd.make_coffee(drink)
from data import MENU
from data import resources


def required(drink):
    '''Fetches the data from MENU'''
    water_needed = MENU[drink]["ingredients"]["water"]
    milk_needed = MENU[drink]["ingredients"]["milk"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    
    cost = MENU[drink]["cost"]
    return 'hehehehheeh'

def restocking():
    water_left += 200
    milk_left += 200
    coffee += 200

def compare():
    if resources_left > ingrdnts:
        water_left - water
        milk_left - milk
        coffee_left - coffee
    else:
        print("Not Sufficient Resources")
        restock = input("Do you want to restock ?? ('yes' or 'no')").lower()
        if restock == "yes":
            restocking()
            compare()
        else:
            #should return them coins 
            []



water_left = resources['water']
milk_left = resources['milk']
coffee_left = resources['coffee']

resources_left = [water_left, milk_left, coffee_left]

money_left = 0

no_cust = False

while no_cust == False:
    drink_choice = input("What would you like? (espresso/latte/cappuccino)\n :").lower()
    if drink_choice == 'off':
        print('Successfully Turned off, Run the Program to Begin Again')
        break
    elif drink_choice == 'report':
        print(f" Water: {water_left}ml\n Milk: {milk_left}ml\n Coffee: {coffee_left}g\n Money: ${money_left}")

    if drink_choice == 'espresso':
        ingrdnts = required('espresso')
    elif drink_choice == 'latte':
        ingrdnts = required('latte')
    elif drink_choice == 'cappuccino':
        ingrdnts = required('cappuccino')
    else:
        print('Please enter a Valid Command')

    water = ingrdnts[0]
    milk = ingrdnts[1]
    coffee = ingrdnts[2]
    price = ingrdnts[3]
    compare()
    

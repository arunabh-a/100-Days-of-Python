from data import MENU
from data import resources


money_left = 0

no_cust = False


def coins():
    quarter_val = int(input("Enter the number of Quarters: ")) * 0.25
    dime_val = int(input("Enter the number of Dimes: ")) * 0.1
    nickel_val = int(input("Enter the number of Nickels: ")) * 0.05
    penny_val = int(input("Enter the number of Pennies: ")) * 0.01
    total = quarter_val + dime_val + nickel_val + penny_val
    return total

def compare(reserves):
    for stock in reserves:
        if reserves[stock] > resources[stock]:
            print("Not Enough Reserves, might want to restock")
        if reserves[stock] <= resources[stock]:
            paid = coins()
            if price > paid:
                print("Not enough paid, payment returned")
            elif price < paid:
                change = paid - price
                print(f"Here's your Change : ${round(change, 2)}")
                resources[stock] -= reserves[stock]
                print(f"Your {drink_choice} is ready")
                break
        


while no_cust == False:
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']

    drink_choice = input("What would you like? (espresso/latte/cappuccino)\n :").lower()
    if drink_choice == 'off':
        print('Successfully Turned off, Run the Program to Begin Again')
        break
    elif drink_choice == 'report':
        print(f" Water: {water_left}ml\n Milk: {milk_left}ml\n Coffee: {coffee_left}g\n Money: ${money_left}")
    elif drink_choice == 'restock':
        for stock in resources:
            resources[stock] += 200
    else:
        drink = MENU[drink_choice]
        price = drink["cost"]
        compare(reserves= drink["ingredients"])
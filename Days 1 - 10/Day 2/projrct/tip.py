#Tip Calculator: Day 2 Project

print ('Welcome to the tip calculator')

bill_amount = input('What was the total bill : ₹')
tip = input('What percentage tip would you like to give: ')
split_people = input('How many people to split the bill: ')

bill_and_tip = int(bill_amount) + int(tip) / 100
payable_amount = round(bill_and_tip) / int(split_people)


print (f'Each person should pay : ₹{payable_amount}')
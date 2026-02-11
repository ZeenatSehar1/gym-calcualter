wallet = 0

add_money = int(input("How much money do you want to add? "))
wallet += add_money

food = int(input("How much money did you spend on food? "))
wallet -= food

transport = int(input("How much money did you spend on transport? "))
wallet -= transport

shopping = int(input("How much money did you spend on shopping? "))
wallet -= shopping

# logical operator check
check = wallet > 500 and wallet < 5000

print("Balance between 500 and 5000:", check)
print("Final wallet balance:", wallet)

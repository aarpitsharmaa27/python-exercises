
        ## Exercise For Shopping Cart Program

item = input("What item would you like to buy ? :")
price = float(input("What's the price ? : "))
quantity = int(input("How many would you like to buy ? :"))

total = price * quantity
print(f"You have bought {quantity} * {item}/s")
print(f"Your total amount is {total}₹")    #For ₹ sign hold ctrl + alt + 4
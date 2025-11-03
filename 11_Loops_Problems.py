# Write a program to find a sum of all the even numbr upto 50.

sum = 0
for i in range (1, 51):
    if i % 2 == 0:
        sum += i

print('The sum of first 50 even numbers is:', sum)


# Write a program to write  first 20 numbers and their squared numbers

for i in range(1,21):
    print(i, i**2)


# Write a program to find sum of first 10 odd numbers using while loop

sum = 0
n = 0
while n <=20:
    if n % 2 != 0:
        sum += n
    n += 1
print("The sum of first 10 odd numbers is :", sum)


# Write a program to check if a number is divisible by 8 and 12 ,upto 100 numbers

for i in range(1,101):
    if i % 8 == 0 :
        print(i, "Number is divisible by 8")
    elif i % 12 == 0 :
        print(i, "Number is divisible by 12")
    else:
        print(i)


# Write program to create a billing system at supermarket

while True :
    name = input("Enter your name: ")
    total = 0
    while True :
        print("Enter the amount and quantity ")
        quantity = int(input("Enter your quantity: "))
        amount = float(input("Enter your amount: "))
        total += quantity * amount
        repeat = input("Do you want to add more items? (y/n): ")
        if repeat == "y"or repeat == "Y":
            continue
        else:
            break

    print("-" * 40)
    print("Name:", name)
    print("Amount to be paid", total)
    print("-"* 40)
    print("**********THANK YOU CUSTOMER**********")

    repeat1 = input("Do you want to go to next customer? (y/n): ")
    if repeat1 == "n"or repeat1 == "":
         break




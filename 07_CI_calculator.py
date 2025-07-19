# Pyhton compound interest calculator

principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print("Please Enter a valid principle amount !!")

while rate <= 0:
    rate = float(input("Enter the rate(in %)e : "))
    if rate <= 0:
        print("Please Enter a valid rate !!")

while time <= 0:
    time = float(input("Enter the time (in years) : "))
    if time <= 0:
        print("Please Enter a valid time (in years) !!")

    amount = principle * (1 + rate / 100) ** time
    print(f"The Total Amount after {time} years is {amount:.2f}₹")

    CI = amount - principle
    print(f"The Total Compound Interest after {time} years is {CI:.2f}₹")


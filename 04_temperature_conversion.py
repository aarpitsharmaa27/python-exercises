
            ## Temperature conversion

temperature = float(input("Enter the temperature :"))
unit = input("Is that temperature is in Kelvin or fahrenhheit ? (K or F) :")

if unit == "K":
    fahrenheit = round((temperature - 273.15) * 9/5 +32 , 3)
    print(f"The temperature is {fahrenheit}°F")      # For degree(°) sign , turn on num lock then hold alt + 0176

elif unit == "F":
    Kelvin = round((temperature - 32) * 5 / 9 + 273.15 , 3)
    print(f"The temperature is {Kelvin}K")

else:
    print("Invalid input")



import math

from Scripts.pywin32_postinstall import root_key_name

# To find circumference of cirlce

radius = float(input("Enter the radius of circle :"))

result = 2 * math.pi * radius

print(f"The circumference is {round(result, 3)}cm")    # 3 means round tp 3 digits


    # To find area of the circle

radius = float(input("Enter the radius of circle :"))

#result = math.pi * radius ** 2
result = math.pi * pow(radius , 2)

print(f"The area of circle is {round(result, 3)}cm²")       # 3 means round tp 3 digits


    # To find Hypotenuse of right angle triagle

a = float(input("Enter the length of base of triangle : "))
b = float(input("Enter the length of perpendicular of triangle :"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenuse of the right angle triangle is {round(c, 3)}cm")


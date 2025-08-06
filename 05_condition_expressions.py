

    #Conditional expression = A one- line shortcut for if-else statement

num = -27
a = 9
b = 27
age =  22
temperature = -20
user_role = "admin"

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "Hot" if temperature >= 20 else "Cold"
print(weather)

login = "Full Access" if user_role == "admin" else "Limited Access"
print(login)


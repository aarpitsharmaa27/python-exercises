

    #Conditional expression = A one- line shortcut for if-else statement

num = 20
a = 6
b = 10
age =  23
temperature = -1
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
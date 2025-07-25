
#------------------Practice--------------

# To made rectangle by any symbol

row = int(input("Enter number of rows :"))
column = int(input("Enter number of columns :"))
symbol = input("Enter symbol :")

for x in range(row):
    for y in range(column):
        print(symbol, end="")
    print()


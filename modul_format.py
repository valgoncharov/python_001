# Строки без переменных
print("first " "second " "third ") #first second third

# Строки в переменных
first = "first"
second = "second"
third = "third"

print(first + second + third) # firstsecondthird

# С пробелами
print(first + " " + second + " " + third) # first second third

first = "first"
second = "second"
third = "third"

# Без пробелов
print(f"{first}{second}{third}") # firstsecondthird

# С пробелами
print(f"{first} {second} {third}") # first second third

print(f"{first} {second} {third.upper()} {10 + 10}") # first second THIRD 20

print("{} {} {}".format(first, second, third)) # first second third

print("%s %s %s" % (first, second, third))
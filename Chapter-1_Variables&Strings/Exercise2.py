# #Take 2 comma seperated input
# 1. Name
# 2. any character

# output - 1. user name length
# 2. count the char that user inputed(bonus: case insensitive count)

#Solutions:

name, char = input("Enter your name and char with comma seperated: ").split(",")
print(len(name))
print(name.lower().count(char.lower()))

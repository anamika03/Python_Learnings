# name = "anamika Singh"

# # len() function
# length = len(name)  #it will also count the space
# print(length)

# # lower() method
# print(name.lower())

# # upper() method
# print(name.upper())

# # title() function
# print(name.title())

# # count() method
# print(name.count("i"))

name2 = "    An  am ika     "
# lstrip() method - discard the left spaces
print(name2.lstrip())

# rstrip() method - discard the right spaces
print(name2.rstrip())

# strip() method - discard the all spaces before and after the string
print(name2.strip())

# replace(" ", "") - replacing the space with no space
name_without_spaces = name2.replace(" ","")
print(name_without_spaces)

# find()
print(name_without_spaces.find("a",3))

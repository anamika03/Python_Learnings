name = "anamika Singh"

# len() function
length = len(name)  #it will also count the space
print(length)

# lower() method
print(name.lower())

# upper() method
print(name.upper())

# title() function
print(name.title())

# count() method
print(name.count("i"))

name2 = "    An  am ika     "
# lstrip() method - discard the left spaces
print(name2.lstrip())

# rstrip() method - discard the right spaces
print(name2.rstrip())

# strip() method - discard the all spaces before and after the string
print(name2.strip())

# replace(" ", "") - replacing the space with no space
new_name = name2.replace(" ","")
print(new_name)

# find()
print(new_name.find("a",3))

# center() method
print(new_name.center(len(new_name)+8 , "*"))
print(new_name.center(15, "*"))
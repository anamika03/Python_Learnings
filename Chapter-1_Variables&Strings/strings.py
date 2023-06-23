name = "Anamika"
last_name = "Singh"
full_name = name + " " + last_name
age = 27
print(full_name)
print(full_name*3) #it will print full_name 3 times
print(name + str(1)) #it will now add 1 in the end

# String Formatting in Python 3
print("hello {}, your age is {} ".format(name, age-2))

# String Formatting in Python 3.6+ versions
print(f"hello {name}, your age is {age*1}")

# String Indexing/Slicing- starts from 0
print(name[3]) #4th character of the name
print(name[:])  #start to end
print(name[1:5])  #1st index to 4th index(5-1)
print(name[1:])  #1st index to end
print(name[:5])  #start to 4th index
print(name[-1])  #last char of the string Negative indexing
# syntax - [start argument : stop argument : step]  step = gap 
# By default step is 1
print(name[-1::-1]) #Reverse the string
print(name[::-1]) #Reverse the string

user_name = input("Name: ")
print(user_name[-1::-1])
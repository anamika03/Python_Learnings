#function

def add_num(x,y):
    return x+y

print(add_num(7,5))
print(add_num("Anamika ","Singh"))
user = input("enter a first name: ")
surname = input("enter surname: ")
print(add_num(user,surname))

#print vs return

def add_three(x,y,z):
    print(x+y+z)

add_three(7,5,12)
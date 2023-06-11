#Greatest of 2 number. Input from user.

def largest_num(x,y):
    if x > y:
        return x
    return y
    
num1 = int(input("enter 1st num: "))
num2 = int(input("enter 2nd num: "))
large_num = largest_num(num1,num2)
print(f"{large_num} is largest")


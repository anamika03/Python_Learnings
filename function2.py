def odd_even(x):
    if x % 2 == 0:
        return "even"
    return "odd"
    
# num = int(input("Enter any num: "))
print(odd_even(8))

def is_even(num):    #num is an argument. During defining the function, value passed is called an argument
    return num%2==0

print(is_even(8))   #8 is a parameter. During the function call value passed is called a parameter

def song():
    return "Happy Birthday Song"
print(song())
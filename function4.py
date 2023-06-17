#default parameter

def main(name,sirname,age):
    print(f"Your name is {name}")
    print(f"Your sirname is {sirname}")
    print(f"Your age is {age}")

main("Anamika","Singh",26)

def main(name,sirname,age=26):  #age is default, if you not pass any argu then it will be default 
                                # and if you pass any value then it will update with the passed argument
    print(f"Your name is {name}")
    print(f"Your sirname is {sirname}")
    print(f"Your age is {age}")

main("Anamika","Singh",27)

def main(name,sirname="unknown",age=27):   #SyntaxError: non-default argument follows default argument
    print(f"Your name is {name}")
    print(f"Your sirname is {sirname}")
    print(f"Your age is {age}")

main("Anamika")  


#Scope
x = 5 #global variable

def main():
    global x   # this is now you are now defining the global var inside the func
    x = 7      #local variable
    return x


print(x)       #print 5
print(main())  #print 7
print(x)       #print 7
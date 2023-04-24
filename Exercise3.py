#EXERCISE - WATCH COCO
#Ask user's name and age
#if user's name start with ("a" or "A") and age is above 10 then
# print "you can watch coco movie"
# else print 'sorry :( you cannot watch coco'

name, age = input("Enter your name and age: ").split()
age1 = int(age)
# name1 = name.lower(()
if age1 > 10 and (name[0]=="a" or name[0]=="A"):  
    print("You can watch COCO movie :)")
else:
    print("Sorry :( you can't watch COCO movie )")
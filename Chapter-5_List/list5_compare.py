# is and == compare lists

fruits1 = ["apple","mango","banana"]
fruits2 = ["apple","mango","banana"]
fruits3 = ["kiwi","apple","grapes","lichi"]
print(fruits1 == fruits2)  # True - values are same
print(fruits1 is fruits2)  # false - both are different objects and have different place in memory
print(fruits1 is fruits3)  # false - both are different objects and have different place in memory
print(fruits2 is fruits3)  # false - both are different objects and have different place in memory
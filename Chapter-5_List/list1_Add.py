fruits = []
# append(object)
fruits.append("apple")
fruits.append("mangoes")
print(fruits)

# insert(index,object)
fruits.insert(2,"kiwi")
print(fruits)

# concatinate
object1 = ["bat","ball"]
object2 = ["choclate","biscuits"]
object = object2 + object1
print(object)
 
# extend - it is an another way of concating list
# object1.extend(object2)  # it will update the object1 with object2 content
# print(object1)
# print(object2)

# Difference between append and extend
# append will concatinate the list within a list and extend concatinate the list items in the another list
object1.append(object2)
print(object1)

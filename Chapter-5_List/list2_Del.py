# Deleting item from list

fruits = ["apple","mango","banana","kiwi","apple","grapes","lichi"]
# pop(index or blank)
fruits.pop()  # remode the last item
print(fruits)

fruits.pop(1)  # remove the 1st index item
print(fruits)  

# remove(object)
fruits.remove("apple")
print(fruits)

# clear
fruits.clear() # It will only remove the items of the list with the empty list
print(fruits)

# delete method
del fruits[2]  # delete the 2nd index item  if you don't pass any value it deletes the whole list
print(fruits)
del fruits  # if you don't pass any value it deletes the whole list and list existance also
print(fruits)  # show error : NameError: name 'fruits' is not defined
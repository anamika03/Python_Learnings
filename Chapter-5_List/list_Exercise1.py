# list of number and in output print the square of the number

# num= [1,2,3,4,5]
# for i in num:
#     print(num[i]*num[i])

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

number = list(range(1,11))
print(square_list(number))

#reverse of the list

def reverse_list(l1):
    rev = []
    for i in l1[::-1]:
        rev.append(i)
        l1.pop()
    return rev

list1 = input("type any thing").split()
print(reverse_list(list1))
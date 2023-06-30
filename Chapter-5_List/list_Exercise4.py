#print the commen item of the list

list1 = [1,2,3,4,5,8,7]
list2 = [3,4,5,6,7,2]

def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder(list1,list2))

#mix and max function and print the difference

num = [3,60,8]
def difference(l1):
    return max(l1) - min(l1)

print(difference(num))
#input --->  [1,2,3,4,5,6,7,8,9]
#output ---> [[1,3,5,7,9],[2,4,6,8]]

input_list = list(range(1,10))
odd = []
even = []
for i in input_list:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
output = [odd, even]
print(output)

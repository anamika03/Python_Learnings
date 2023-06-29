# list["abc","lmn","xyz"] -----> list["cba","nml","zyx"]

list1 = ["abc","lmn","xyz"]
list2 = []
for i in list1:
    list2.append(i[::-1])
print(list2)
              
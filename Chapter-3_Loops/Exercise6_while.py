# Enter a Name
# Ex - Anamika Singh
# print count od each words
# output: A:3
#         n:2
#         m:1
#         i:2
#         k:1
#         s:1
#         g:1
#         h:1
#     space:1

name1 = input("enter your name: ")
name = name1.lower()
i = 0
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
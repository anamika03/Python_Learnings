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

name = input("Ener your name: ")
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
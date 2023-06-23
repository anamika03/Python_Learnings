# user enter number
# then sum the number

num = input("Ener a num more the 1 digit : ")
sum = 0
for i in range(0,len(num)):
    sum += i

print(f"sum of the num : {sum}")    
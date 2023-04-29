#ask user to input num containing more than 1 digit
# like 1234, 456
# calculate= 1+2+3+4 and print

num = input("enter a num containing more than 1 digit: ")
sum = 0
i = 0
while i < len(num):
    sum += int(num[i])
    i += 1
print(f"sum is {sum}")

#print the sum of n number enter by the user

num = int(input("Enter the natural number: "))
i = 1
sum = 0
while i<=num:
    sum += i
    i += 1
print(f"Sum of the natural number is {sum}")
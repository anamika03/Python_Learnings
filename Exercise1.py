#Ask user to input 3 numbers and you have to print average of 3 numbers using string formatting.

num1, num2, num3 = input("3 numbers seperated by comma: ").split(",")
average = (int(num1) + int(num2)+ int(num3))/3
print(f"Average of 3 number is {average}")





num1 = int(input("Enter  Divsier:"))
num2 = int(input("Enter Divident:"))
try:
    result = num2 / num1
    print(result)
except ZeroDivisionError:
    print("Error! Division by zero")

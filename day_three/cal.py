
num1 = int(input("Enter first number:"))
op = input("Enter Operation(+,-,/,*):")
num2 = int(input("Enter second number:"))
           
if op == "+":
    print(num1, num2, "=", num1+num2)
elif op == "-": 
    print(num1, num2, "=", num1-num2)
elif op == "*":
    print(num1, num2, "=", num1*num2)
elif op == "/":
    if num2 != 0:
        print(num1, num2, "=", num1/num2)
    else:
        print("Error! Division by zero")
else:
    print("Error! Invalid operator")
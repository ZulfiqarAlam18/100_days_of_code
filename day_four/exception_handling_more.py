
try:
    num1 = int(input("Enter your Age in numbers :"))
    if num1 >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
except ValueError:
    print("Invalid input! Age should be a number")
            
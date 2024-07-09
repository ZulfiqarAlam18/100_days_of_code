import re

def validator(email):

    #Regex pattern
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

while True:
    gmail = input("Enter your email address to validate or 'exit' to terminate: ")

    if gmail.lower() == "exit":
        break

    if validator(gmail):
        print("Valid email address")
    else:
        print("Invalid email address")

#one way
try:
    count = 1
    total_cost = 0
    no_of_items = int(input("Enter number of items:"))
    while count <= no_of_items:
        price = int(input(f"Enter price of item no.{count} :"))
        total_cost += price
        count += 1
    print("Total cost: ", total_cost)
except ValueError:
    print("Input Error")
        

#Antoher way of doing the same thing through using a list:

try:
    count = 1
    total_cost = 0
    price_list = []
    no_of_items = int(input("Enter number of items:"))
    while count <= no_of_items:
        price = int(input(f"Enter price of item no.{count} :"))
        price_list.append(price)
        count += 1
    total_cost = sum(price_list)
    print("Total cost: ", total_cost)
except ValueError:
    print("Input Error")
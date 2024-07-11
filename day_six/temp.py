
#Method to convert celsius to fahrenheit
def cel_to_fah(celsius):
    return (celsius * 9/5) + 32

#method to convert fahrenheit to degrees(celsius)
def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

#taking user input to convert either celsius to fahrenheit or fahrenheit to celsius
input = input("Press 1 to go from celsius to fahrenheit and press 2 to go from fahrenheit to celsius")

if input == "1":
    print(cel_to_fah(input))
elif input == "2":
    print(fah_to_cel(input))
else:
    print("Invalid input!")
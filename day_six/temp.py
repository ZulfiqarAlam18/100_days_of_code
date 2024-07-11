
#Method to convert celsius to fahrenheit
def cel_to_fah(celsius):
    return (celsius * 9/5) + 32

#method to convert fahrenheit to degrees(celsius)
def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

#method to convert degrees(celsius) to Kelvin
def cel_to_kel(celsius):
    return celsius + 273.15



#method to convert Kelvin to degrees(celsius)
def kel_to_cel(kelvin):
    return kelvin - 273.15

#taking user input to convert either celsius to fahrenheit or fahrenheit to celsius
input = input("Press :\n1. Cel to Frahrenheit \n2. Celsius to Frahrenheit \n3. Cel to Kelvin \n4. Kelvin to Celsius\nNote:Press any number from above data:")

if input == "1":
    print(cel_to_fah(input))
elif input == "2":
    print(fah_to_cel(input))
elif input == "3":
    print(cel_to_kel(input))
elif input == "4":
    print(kel_to_cel(input))
    
else:
    print("Invalid input!")
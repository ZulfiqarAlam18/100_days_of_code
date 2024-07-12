# program for trafffic signal colors 

color = input("Enter color:")

if color.lower() == "red":
    print("Stop")
elif color.lower() == "green":
    print("Go")
elif color.lower() == "yellow":
    print("Caution")
elif color.lower() == " cyan":
     print("Ready")
else:
    print("Invalid color")


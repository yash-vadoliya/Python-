#7) The distance between two cities is input through keyboard. Write a program to convert and print this distance in feet, meter, inch and centimeter.


distance_in_miles = 25

distance_in_feet = distance_in_miles * 3280.84
distance_in_meters = distance_in_miles * 1000
distance_in_inches = distance_in_miles * 39370.1
distance_in_cm = distance_in_miles * 100000

print(f"Distance in feet: {distance_in_feet} feet")
print(f"Distance in meters: {distance_in_meters} meters")
print(f"Distance in inches: {distance_in_inches} inches")
print(f"Distance in centimeters: {distance_in_cm} centimeters")
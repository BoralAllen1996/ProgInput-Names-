# A Python program to convert the distance (in feet) to inches, yards, and miles.

#Conversion input details...
#You may input any numbers of distance to convert into inches , yards and miles......

d_ft = int(input("Enter the distance in feet:" ))

#Conversion 

d_inches = d_ft * 12               #The distance in inches.
d_yards = d_ft / 3                 #The distance in yards.
d_miles = d_ft / 5280              #The distance in miles.

#conversion processof result..........

print(d_inches)
print(d_yards)
print(d_miles)

#end of conversion..........
#Program input name to last name info..............................

first_name = str(input("Please Enter your first name:"))
middle_name = str(input("Please Enter your middle name:"))
last_name = str(input("Please Enter your last name:"))


first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s} {last}"

#Command to execute the program..............
print("\nHello,\n\n\n", name_format.format(first=first_name, middle=middle_name, last=last_name), "Welcome!\n")
print("Thank you for providing to us your information details.", "Have a good day!\n")

#end...
    
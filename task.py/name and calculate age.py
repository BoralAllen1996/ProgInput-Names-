name=input("Enter your name please? ")
print(name,  "Hi Thank you!")
input("How are you today: ")

print("That's great!")

from datetime import date
date_of_birth = int(input("In which year you took birth: "))

today_date = date.today().strftime("%Y")

print("Your current age is ",int(today_date)-date_of_birth)
print("Thank you , Have a good day!")
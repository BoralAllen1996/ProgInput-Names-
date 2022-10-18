from datetime import date

Name =input("Enter your name: ")
print(Name)
print("Thank you !")

def age(yearborn):
    return date.today().year - yearborn

yearborn = int(input("Enter your birth year: "))

print(f" you are {age(yearborn)} years old")

# Thank you....
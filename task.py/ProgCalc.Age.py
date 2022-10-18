from datetime import date

Name =input("Enter your name: ")
print(Name)

def age(yearborn):
    return date.today().year - yearborn

yearborn = int(input("Enter your birth year: "))

print(f" you are {age(yearborn)} years old")

count=0
A=int(input("Enter the number:\n"))
for i in range (1,A+1):
 if A%i ==0:
    count+=1
if count ==2:
      print("Entered number is prime! ")
else:
    print("Entered number is not a prime! ")
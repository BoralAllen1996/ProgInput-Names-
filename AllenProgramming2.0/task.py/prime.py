x=int(input("number=?"))
if x==1:
    print("neither prime nor composite")
elif x==2:
   print("Prime")
else:
   for i in range(2,x):
     if x%i==0:
        print("Not prime")
        break
     else:
        print("Prime")
        break
        
        end
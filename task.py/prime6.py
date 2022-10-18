val = int(input('Enter the value:\n')) 
j = 0
for i in range(1,val+1):
  if j >=2:
     print (f'{val} is not a prime number') 
     break
  if val%i==0:
     j+=1
else:
    print(f'{val} is a prime number')
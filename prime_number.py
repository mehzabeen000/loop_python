num=int(input("Enter the number"))
counter=2
while counter<=num:
    if num%counter==0:
        print("Not a prime number")
        break
        counter+=1
    else:
        print("It is a prime number")
        break
    
#we have to see whether the input is prime number or not

num=int(input("Enter the number"))
counter=1
count=0
while counter<=num:
    if num%counter==0:
        count+=1
    counter+=1
if count==2:
    print("It is a prime number")
else:
    print("It is not a prime number")
    
        
    
    
    
    

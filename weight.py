weight=0
sum=0
while weight<11:
    p=int(input("Enter the number"))
    sum=sum+p
    weight+=1
    print(sum)
    x=sum/11
    print(x)
if x%5==0:
    print("It is divisible by 5")
else:
    print("It is not divisible by 5")
    
#we have to take 11 input of weight and take the average of it
#and check whether the average is a multiple of 5 or not

    


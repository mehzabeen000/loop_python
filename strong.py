#we have to check whether the particular number is a strong number or not

num=int(input("Enter the number"))
sum=0
temp=num
while num>0:
    i=1
    fac=1
    remainder=num%10
    while i<=remainder:
        fac=fac*i
        i+=1
    sum=sum+fac
    num=num//10
if sum==temp:
    print("It is a strong number")
else:
    print("It is not a strong number")
    
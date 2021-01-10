#we have to check whether the particular number is armstrong or not

num=int(input("Enter the number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
    
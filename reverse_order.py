#We have to print the number in reverse order
#1st Method
num=int(input("Enter"))
counter=0
while num>0:
    a=num%10
    counter+=1
    num=num//10
    print(a)
    
#2nd Method
num=int(input("Enter the number"))
counter=0
while num>0:
    a=num%10
    counter=(counter*10)+a
    num=num//10
    print(counter)
    

    
guess=1
num=15
while guess<=10:
    sum=int(input("Enter your guess\n"))
    if sum==num:
        print("Your guess is right,You won\n")
        break
    elif sum>num:
        print("Too high.Try Again\n")
    else:
        print("Too low.Try Again\n")
    
#We have to make a guessing game in which we have to guess the 
#particular guess is right or wrong and it will give output 
#according to the input (say lower or greater) unless guess is right.

    
    
        
    
    
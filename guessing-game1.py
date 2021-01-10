guess=1
while guess<=5:
    sum=int(input("Enter your guess\n"))
    if sum==16:
        print("Your guess is right,You won\n")
        break
    else:
        print("Your guess is wrong.Try Again\n")
    guess+=1
else:
    print("You lose")
    
#We have to make a guessing game in which we have to guess the 
#particular number is right or wrong and we will be provided with 5 chances

    
    
        
    
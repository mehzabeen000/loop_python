#we have to print the pattern
#1st Method
counter=1
while counter<=5:
    print('*' * counter)
    counter+=1
    

#2nd Method
num=int(input("Enter"))
counter=1
while counter<=num:
    print('*' * counter)
    counter+=1
    

#3rd Method for printing the reverse pattern
num=int(input("Enter"))
while counter>0:
    print("*" * counter)
    counter-=1
    
#4th Method for printing the pattern in different ways 
num=int(input("Enter"))
counter=1
while counter<=num:
    print((" ")*(num-counter)+(counter*'*'))
    counter+=1
    

    
    
    
    
    


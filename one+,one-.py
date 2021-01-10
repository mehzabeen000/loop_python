counter=0
sum=1
while counter<=100:
    counter+=2
    sum=sum-2
    print(sum,counter)
    
#We have to make output one negative and one positive number from 1 to 100
#ex -1,2,-3,4 etc.

counter=0
while counter<=100:
    if counter%2==0:
        print(counter*-1)
    else:
        print(counter)
    counter+=1
    
        
    

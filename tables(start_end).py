start=int(input("Enter number from where you want to start the table"))
end=int(input("Enter number from where you want to end the table"))
while start<=end:
    i=1
    while i<=10:
        print(start, '*' ,i,"=",start*i)
        i+=1
    start+=1
    print(".................")
    
#we have to take 2 numbers and print the tables
#from one(start) particular number to another(end) number
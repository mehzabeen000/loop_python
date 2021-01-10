#we have to print the particular pattern.
#1st way
one="1"
zero="0"
i=3
while i>=0:
    print(i*(one+zero)+"1")
    i-=1
    
#2nd way
one="1"
zero="0"
i=1
while i<=5:
   print((" ")*(5-i)+((one+zero)*i))
   i+=1
    
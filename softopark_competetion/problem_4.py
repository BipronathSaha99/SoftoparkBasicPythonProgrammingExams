#prim prime number
#input
num=int(input("enter any number:"))

#logic
#if num is grater than 1
if num>1:
    #iterate from 2 to n/2 
    for i in range(2,num):
        #if num is divisble by any number is not prime 
        if num%i==0:
            print(f"{num} is a composite number")
            break
    else:
        print(f"{num} is a prime number")

else:
    print(f"{num} is a composite number")
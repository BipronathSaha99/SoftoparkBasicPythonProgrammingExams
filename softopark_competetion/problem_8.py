#print the gcd between two numbers 

#input
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))

#find minimum number
mn=min(num_1,num_2)

for i in range(1,mn+1):
    if (num_1%i==0) and(num_2%i==0):
        gcd=i


print(f"The gcd between {num_1} and {num_2} is {gcd}")


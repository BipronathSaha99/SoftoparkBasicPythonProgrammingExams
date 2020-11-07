#print the lcm between two numbers 

#input
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))

#find maximum number
mx=max(num_1,num_2)

while True:
    if (mx%num_1==0) and(mx%num_2==0):
        break
    mx=mx+1

print(f"The lcm between {num_1} and {num_2} is {mx}")
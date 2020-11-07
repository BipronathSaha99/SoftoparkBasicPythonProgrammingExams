''' 
একটি ক্যালকুলেটর তৈরি করতে হবে যেখানে যোগ,বিয়োগ,গুণ,ভাগ করার জন্য মেথড থাকবে।
''' 
def cal(num_1,num_2,op):
    if op=='+':
        return num_1+num_2
    elif op=='-':
        return num_1-num_2
    elif op=='*':
        return num_1*num_2
    else:
        return num_1/num_2

#input
num_1=float(input("Enter first number:"))
num_2=float(input("Enter second number:"))
op=input("Choose an opertor (+,-,*,/):")

#output
print("Sum=",(num_1+num_2))
print("Sub=",(num_1-num_2))
print("Mul=",(num_1*num_2))
print("Div=",(num_1/num_2))
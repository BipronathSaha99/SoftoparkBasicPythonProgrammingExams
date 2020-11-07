'''  
ইউজার এক লাইনে তিনটি পূর্ণ সংখ্যার ইনপুট দিবেন সবচেয়ে বড় সংখ্যা বের করতে হবে।
'''
#input

num_1,num_2,num_3=input().split()
num_1=int(num_1)
num_2=int(num_2)
num_3=int(num_3)

#logic
if (num_1>num_2 and num_1>num_3):
    print(f"{num_1} is the largest number")
elif (num_2>num_1 and num_2>num_3):
    print(f"{num_2} is the largest number")
else:
    print(f"{num_3} is the largest number")

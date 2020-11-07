'''ইউজার একটি পুর্ন সংখ্যা ইনপুট দিবে সংখ্যা জোর হলে আউটপুট হবে(even)
আর বিজোড় হলে আউটপুট হবে (odd)'''

#input
num=int(input("Enter the number:"))
#logic
if (num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
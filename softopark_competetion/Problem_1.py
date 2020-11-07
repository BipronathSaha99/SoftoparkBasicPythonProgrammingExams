#ইউজার যেকোনো একটি পূর্ণসংখ্যা  ইনপুট দিবে আর এই পূর্ণসংখ্যার নামতা আউটপুট দেখাতে হবে।
#input
num=int(input("Enter number:"))
count=1
while count<=10:
    print(str(num)+'x'+str(count)+'='+str(num*count))
    count=count+1
    
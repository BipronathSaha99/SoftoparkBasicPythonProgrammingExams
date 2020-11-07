'''A={1,2,3,4,5},B={5,6,7,8} union and intersection() ফাংশন (method) ব্যবহার না করে তাদের 
ইউনিয়ন ও ইন্টারসেকশন সেট C বের কর'''

#input
A={1,2,3,4,5}
B={5,6,7,8}

#logic
#union set of A & B sets
C=A|B
#output of union set
print(f"Union of {A} and {B} sets is {C}")

#intersection set of A & B sets
C=A&B
#output of intersection set
print(f"Intersection of {A} and {B} sets is {C}")

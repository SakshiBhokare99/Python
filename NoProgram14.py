# Spy number
# logic :
# digit sum == digit product

num=217
sum=0
product=1

while num>0:               # 1 3 2  
    rem=num%10             #2   3  1
    sum=sum+rem            # 2+0=2  3+2=5   5+1=6
    product=product*rem    # 2*1=2  2*3=6   6*1=6
    num=num//10            # 13  1 0

if sum==product:
    print("No is spy")
else:
    print("No is not spy")
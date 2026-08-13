# check no is palindrome or not

num=121
rev=0
temp=num

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num//=10

if rev==temp:
    print("No is palindrome")
else:
    print("No is not palindrome")
# Neon no : no where sum of digits of square is equal to the original number
# ex : 
# no : 9
# square : 81
# sum of digit : 8+1=9

num=int(input("Enter any no:"))
square=num**2       # 9**2=81
sum=0
while square>0:        #81>0  1>0 
    digit=square%10    # 8 1 
    sum+=digit         #8+0=8  8+1=9
    square//=10        # 1 0

if sum==num:
    print("it is neon no")
else:
    print("It is not neon no")
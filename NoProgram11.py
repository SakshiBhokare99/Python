# Happy no : no that eventually become 1 when replace by sum of square of its digit repeatedly
# ex:
# 19 : 1**2+9**2= 82
# 82 : 8**2+2**2 = 68
# 68 : 6**2+8**2 = 100
# 100 : 1**2+0**2+0**2 = 1

num=int(input("enter any no:"))
sum=0
temp=num

while num!=1 and num!=4:

    while num>0:
        digit=num%10
        sum+=digit**2
        num//=10

    num=sum

if num==1:
    print(temp,"is happy no")
else:
    print(temp,"is not happy no")
    

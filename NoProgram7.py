# Armstrong no : 153
# find length : 3
# find power of 1,5,3 
# 1**3=1 , 5**3=125, 3**3=27 
# add power values 1+125+27=153

num=1634
count=0
sum=0
temp=num
while num>0: 
    count+=1  
    num//=10  
print(count)
num=temp
while num>0:
    rem=num%10
    cube=rem**count
    sum+=cube
    num//=10
if temp==sum:
    print("no is armstrong")
else:
    print("no is not armstrong")


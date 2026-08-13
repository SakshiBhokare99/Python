# digit sum
num=1234
sum=0

while num>0:
    rem=num%10
    sum+=rem
    num=num//10
print(sum)

# In python there are 2 division method
#1. normal division : normal division
#2. Floor division : that convert decimal into complete no
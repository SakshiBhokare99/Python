# factors : no which is completely divisible
num=6
i=1
while i<=num:
    if num%i==0:
        print(i)
    i+=1


num=4
for i in range(1,num+1,1):
    if num%i==0:
      print("Factors of 4:",i)
    
# Find facorial:
#5=5*4*3*2*1

num=5
i=1
fact=1
while i<=num:
    fact*=i
    i+=1
print("Factorial of 5:",fact)


num=7
fact=1
for i in range(1,num+1,1):
    fact*=i
print("Factorial of 7:",fact)
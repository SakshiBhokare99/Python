# Fibonacci series
num=10
a=0
b=1
count=0
print("Fibonacci series: ")

while count<=num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1
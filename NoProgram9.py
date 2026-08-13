# Prime no
num=int(input("Enter any no:"))
i=2
flag=1 
if num<=1:
    flag=0
else:
    while i<num:
        if num%i==0:
            flag=0
            break
        i+=1
if flag:
    print("Prime no")
else:
    print("Not prime no")
        


 
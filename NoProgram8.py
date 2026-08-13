# perfect no : A number that is equalto the sum of its proper factors
# Ex: 

num=6
sum=0
i=1
while i<num:        
    if num%i==0:  
        sum+=i
    i+=1

if num==sum:
    print("Perfect no")
else:
    print("Not perfect no")

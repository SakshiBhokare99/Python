# 1234-->Digits -->count 
num=1234
count=0
while num>0: #1234 123 12 1
    count+=1  #1 2 3 4
    num//=10  #123 12 1
print(count)
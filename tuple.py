x=(10,20,30,40)
print(x)
print(x[0])

# # loop
for i in x:
    print(i)

for i in range(len(x)):
    print(i)
    print(x[i])

# 2 methods : count, index
# rows print:
x=((12,13,14),(21,25,30))
for i in x:
    print(i)

# index with value print:
index=0
for i in x:
    for j in i:
        index+=1
        print(index,"-",j)


x=((10,20),(41,(42,43)),[10,20])
print(x[2][1])
print(x[1][0])
print(x[1][1])
print(x[1][1][1])

# nested loop:
for mainitem in x:
    for subitem in mainitem:
        if type(subitem)==tuple:
            for item in subitem:
                print(item)
        else:
            print(subitem)

# #1. update 101=205
x=((10,20),(41,(42,43)),[101,201])
x[2][0]=205
print(x)

mul=1
sum=0
rem_ele=0
x[2][0]=405
for mainitem in x:
    if type(mainitem)==tuple:   
        for subitem in mainitem:
            if type(subitem)==tuple:
                for item in subitem:
                    mul*=item
            else:
                rem_ele+=subitem
    else:
        for item in mainitem:
            sum+=item
print(sum)
print(mul)
print(rem_ele)

new_sum=0
while(rem_ele>0):
    new_sum+=rem_ele%10
    rem_ele//=10

print(new_sum)






    

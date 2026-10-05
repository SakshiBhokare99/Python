#find the length of list
x=[]
len=0
size=int(input("Enter size of element:"))
for i in range(size):
      ip=int(input("Enter elemnt to add:"))
      x.append(ip)
      len+=1
print(x,len)


# count the presece of element:
x=[10,20,10,3,4]
ct=0
ip=int(input("Enter element to calc count"))
for i in x:
    if ip==i:
        ct+=1
print(ip,ct)
    

# Calculate total of list element
x=[10,20,30,40]
sum=0
for i in x:
    sum+=i
print("Sum:",sum)


#Find max min list
x=[10,20,4,35]
max=0
for i in x:      
    if i>max:    
        max=i    
print(max)

min=x[0]
for i in x:
    if i<min:
        min=i
print(min)

#print duplicate element:
x=[30,40,30,70,50,40]

for i in range(len(x)):
   ct=0
   for j in range(len(x)):
        if x[i]==x[j]:
            ct+=1

   if ct>1:
        ct1= 0
        for k in range(i):
            if x[k]==x[i]:
                ct1=1

        if ct1 == 0:
            print(x[i])




# create a list by taking user input
x=[]
size=int(input("enter the size to create list:"))
for i in range(size):
   ip=int(input("Enter elemnt to add:"))
   x.append(ip)
print(x)


# remove duplicate and print unique element of list
x=[21,23,24,21,25]  
unique=[]  
for i in x:    
    if i not in unique:   
        unique.append(i) 
print(unique)

# remove element without remove method
x=[21,23,24,21,25]  
unique=[] 
ip=int(input("Enter element to remove:")) 
for i in x:    
    if i != ip:   
        unique.append(i) 
print(unique)


# number program:

# sum of element:
x=[10,20,30,40,89,10,100]
sum=0
for i in x:
    sum+=i
print("Sum:",sum)

#odd element sum:
sum=0
for i in x:
    if i%2!=0:
        sum+=i
print("odd sum:",sum)



#replace eleemnt:
for i in range(len(x)):  #0-7(6) 10 20 30
    if x[i]==30:   #10==30 20==30 30==30(t)
        x[i]=0
print(x)

#reverse list 
# x.reverse()
# print(x)
x=[20,30,10]
rev=[]
for i in range(len(x)-1,-1,-1):
    rev.append(x[i])
print(rev)

# remove duplicate element
x=[21,23,24,21,25]  # [21,23,24,25]
unique_ele=[]  # 21 23 24 25
for i in x:    #21 23 24 21 25
    if i not in unique_ele: 
        unique_ele.append(i) 
print(unique_ele)


#x=[31,32]
#y=[33,34] merge list without inbuilt
x=[31,32]
y=[33,34]
z=[]

for i in x:
    z=z+[i]
for i in y:
    z=z+[i]
print("marge list:",z)




# frequency 10:2 20:1 30:2 40:1
x = [10, 20, 10, 30, 40, 30]

for i in range(len(x)):
    count = 0
    already = 0

    for k in range(i):
        if x[i] == x[k]:
            already = 1

    if already == 0:
        for j in range(len(x)):
            if x[i] == x[j]:
                count += 1

        print(x[i], ":", count)





x=[10,20,30]
print(x)

print(x[1])

# update
x[2]=300
print(x)

y=[10,"hi",90.78,True]
print(type(y))

# for loop
for i in range(len(y)):
    print(y[i])

# Functions 
# len  min  max  sum  sorted
x=[20,10,30]
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
print(sorted(x))
print(sorted(x,reverse=True))


# Methods : 
#1.Appeend (add after last element)
x=[]
print(x)
x.append(10)
print(x)

#2.Extend (merge list)
x.extend([3,4])
print(x)

#3. Copy
y=x.copy()
print(y)

#4. Count 
print(x.count(10))

#5. Insert (Add element to particular index)(index , value)
x.insert(1,5)
print(x)

# Delete operation Method:
#1. Remove: (particular element remove)
x=[20,30,40]
x.remove(20)
print(x)

#2. Pop (by default last element remove)
x.pop()
print(x)

#3. clear (remove all element)
x.clear()
print(x)


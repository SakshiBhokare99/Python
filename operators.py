sen = '''Hello my name is sakshi
         i am learning python '''
print(sen)

# Operators
# Arithmatic operators
a=10;
b=5;
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# Comparison / relational operators
a=20
b=15
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#Assignment operator
a=2
b=4
a+=4 
print(a)

b-=2
print(b)

y=20
y/=10
print(y)

z=124
z-=5  #119
z*=2  #238
z+=4  #242
z/=9  #26
z%=3  #2.88
print(z)

#logical operator
a=10
b=20
print(not(a>b and b<a)) #F
print(a>b or b<a)  #F
print(b>a and a<b or a==b) #T

#Bitwise operator
print(7&4)  #bitwise and
print(2|3)  #bitwise or
print(2^3) #bitwise xor
print(~5)   #bitwise complement not

#Membership operator
# in operator
x=[10,20,30,40]
print(20 in x)
print(50 in x)

#not in operator
print(50 not in x)
print(20 not in x)

#Identity operator
x=[1,2,3,4]
y=x
z=[5,6,7]
print(x is y)
print(x is z)
print(x is not z)

print("hello", end=" ")
print("world")















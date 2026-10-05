# fetch character in string:
city="pune"
for i in city:
    print(i,end=" ,")


# print vovels in string: 
state="gujrat"
for ch in state:
    if ch in 'aeiouAEIOU':
        print(ch)


# find count of vowels of string:
x="India"
ct=0
for ch in x:
    if ch in 'aeiouAEIOU':
        ct+=1
print(ct)


# string inbuilt method
#1. length
color='black'
print(len(color))

#2. Upper case
print(color.upper())

#3. isupper
print(color.isupper())

#3. lower case
print(color.lower())

# 4. swapcase : lowercase into uppercase nd uppercase into lowercase
x="hELLo" 
print(x.swapcase())

#5. find index if present
print(x.find('E'))

#6. not existing charater represent default value as -1
print(x.find('s'))

#7. count how many times a character is present in string
print(x.count('L'))

#8. index method 
# in index and find method there is difference is:  In find method if 
# character not exist then its return -1 but in index method its return error
print(x.index('L'))
#print(x.index('s'))

# true/false : checking methods
#1. isalpha : check completely alphabet or not
x="abc123"
print(x.isalpha())
y="abcd"
print(y.isalpha())

#2. isnumeric : check completely number or not
x='abc123'
print(x.isnumeric())
z='1234'
print(z.isnumeric())

#3. isalnum : combination of letters and numbers
x='abc123'
print(x.isalnum())

#string : startwith : check start value / endwith : check ending value
a="python"
print(a.startswith('p'))
print(a.startswith('y'))

print(a.endswith('n'))

# replace letters with another
print(a.replace('t','T'))
x="apple"
print(x.replace('p','x'))

a="Apple"
print(x.islower())



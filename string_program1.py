# count no of char
x="stringprogram"
ct=0
for ch in x:
        ct+=1
print(ct)


# reverse a string
x="hello"
print(x[::-1])

# level --> check palindrome or not
x="level"
temp=x[::-1]
if x==temp:
        print("It is palindrome")
else:
        print("it is not palindrome")

# char replace  
z="maharashtra"  # replace a with x  
#print(z.replace('a','x'))
op=" "
for ch in z:
   if ch=='a':  #m!=a a==a h!=a a==a r!=a a==a s!=a h!=a t!=a r!=a a==a
        op+='x' 
   else:
        op+=ch  # mhrshtr
                        
print(op)

# swap characters upper to lower
ip="HelLo"
op=" "
for ch in ip:
      if ch.islower():
            op+=ch.upper()
      else:
            op+=ch.lower()
print(op)

# print duploicate character 
ip='maharashtra'
for ch in set(ip):
       if  ip.count(ch)>1:
            print(ch)
   




                 

        

#1. without arg without return type :
def greet():
    print("GE!")
greet()

# #2. with arg without return type:
def sq(num):
    square=num*num
    print(square)

num=int(input("enter no to find square:"))
sq(num)


#3. with arg with return type:  use to reuse the function
def power(baseno,raiseno):
    pow=baseno**raiseno
    return pow

# #1 way:
print(power(3,3))

# #2. way:
op=power(2,3)
print(op**2)


# #4. Positional argument
def bio(name,age):
    print(f"name:{name},age:{age}")

# #manually:
bio("ram",20)  #ram 20

#  user ip:
n_ip=input("enter yr name:")
a_ip=int(input("enter yr age:"))
bio(n_ip,a_ip)

# #positional argument:
bio(age=a_ip,name=n_ip)

# default argument
def welcome(inst="Linkcode"):
    print(f"Welcome {inst}!")

welcome("linkcode tech")
welcome()
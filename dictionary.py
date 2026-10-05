x={}
print(x,type(x))

#Add
x["Id"]=101
x["name"]="ram"
print(x)

# value access : dict_name["id"]
print(x["name"])

#update : dict_name["id"]=newvalue
x["name"]="Sita"
print(x)

# Methods: dobj.methodname()
stud={
    "rollno":101,
    "name":"ram",
    "city":"Pune",
    "marks":90.89
}

print(stud)

#1. keys()  : only keys
print(stud.keys())

#2. values()  : only values
print(stud.values())

#3. items()  : key:value pair(wrapes in tuple form)
print(stud.items())

#Loop :
# return keys only  #by default keys return if any variable is used 
for keys in stud:
    print(keys)

# return values only
for values in stud.values():
    print(values)

# return Key : value pair
for k,v in stud.items():
    print(f"{k}:{v}")

# update:
stud.update({"marks":100})
stud.update({"sub":"Python"})
print(stud)

#Remove methods:
#pop([key]) : return key and return value
print(stud.pop("sub"))
print(stud)

print(stud.popitem())
print(stud)

del stud["city"]
print(stud)

print(stud.clear())
print(stud)


stud={
    "rollno":101,
    "name":"ram",
    "marks":(90,99,100),
    "sub":["java","python","html"],
    "address":{
        "city":"pune",
        "state":"maharashtra",
        "country":"India",
        "pincode":411011

    }
}

#Print name of country #india
print(stud["address"]["country"])

# print subject python:
print(stud["sub"][1])

#html marks 
print(stud["marks"][2])

#addition of java and python
print(stud["marks"][0]+stud["marks"][1])






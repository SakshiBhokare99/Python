# reverse string without inbuilt function
x="hello"
rev=" "
for ch in x:
    rev=ch+rev
    #h+""=h
    #e+h=eh
    #l+eh=leh
    #l+leh=lleh
    #o+lleh=olleh

print(rev)


# remove duplicate character -- hello -->helo-->l
a="hello"
op=""
for ch in a:  #h e l l o
    if ch not in op: # h e l l o
        op+=ch  #helo
print(op)

#print("x" in "bye")
#print("x" not in "bye")

# calculate words in string
a="I, like, python, programming"
print(a)
words=a.split(",")
print(words)
print(len(words))

str1="python_is_easy_to_learn"
words=str1.split("_")
print(words)
print(len(words))


# find largest word in string 
str2="python is interpreted language"
words=str2.split()  # python is interpreted language
largest_word=""  #""
for ch in words:   #python is interpreted language
    if len(ch)>len(largest_word):  #6>0(t) 2>6(f) 11>6(t) 8>11(f)
        largest_word=ch  #python interpreted
print(largest_word)

# character how many times occur 
#hello --> h:1 e:1 l:2 o:1
str3="hello"
freq={}
for ch in str3:  # h e l l o
    if ch in freq:  #h e l l o
        freq[ch]+=1
    else:
        freq[ch]=1  #h:1 e:1 l:2 o:1
print(freq)





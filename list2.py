x=[[101,102,103],[201,202,203],[301,302,303]]
#       0               1             2
# print(x)
# print(x[1][1])

# # update 
# x[2][2]=403
# print(x)

# # append
# x.append([401,402,403])
# print(x)

# print(x[1])

# # Nested loop:
# for i in x:
#     for j in i:
#         print(j,end=" ")
#     print()


# # sum of all elements:
# sum=0
# for i in x:
#     for j in i:
#         sum+=j
# print("Sum is:",sum)

# # print nos divisilbe by 5
# flag=0
# for i in x:
#     for j in i:
#         if j % 5 ==0:
#             print(j)
#             flag=1


# if flag==0:
#     print("Not divisible by 5")


# # rowwise element count : 1st floor has 3 rooms
# floor=0
# for i in x:
#     ct=0    # for update loop
#     for j in i:
#         ct=+1
#     floor+=1
#     print(f"floor {floor} has {ct} rooms.")

# each rowwise sum : 101+102+103
row=0
for i in x:
    sum=0
    for j in i:
        sum+=j
    row+=1
    print(f"sum of row {row} is {sum}")

# each col wise sum : 101+201+301
col=0
for j in range(3):
    sum=0
    for i in range(3):
        sum+=x[i][j]
    col+=1
    print(f"Sum of col {col} is {sum}")

# diagonal sum : (2 diagonals)
sum=0
sum1=0
for i in range(len(x)):          #3
    for j in range(len(x[i])):   #[,,]==3
        if i==j:                #i=0&j=0(t) i=0&j=1(f)
            sum+=x[i][j]        #x[0][0]=101  x[1][1]=202  x[2][2]=303
        if i+j==2:
            sum1+=x[i][j]       
print("sum of diagonal:",sum,sum1)


# count sum & print element on even index and oddindex
 
# border element chi sum internally nd subtract middle element
sum=0
for i in range(len(x)):      #len passes index 
    for j in range(len(x[i])):
        if i==0 or i==len(x)-1 or j==0 or j==len(x)-1:
            sum+=x[i][j]

print("Sum is:",sum)
mid=len(x)//2
print(sum-x[mid][mid])









        

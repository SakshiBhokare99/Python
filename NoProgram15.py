# Number Program

print("Number Program\n1.Perfect No\n2.Palindrome No\n3.Factorial\n4.Spy No\n5.Neon no\n6.Exit")
choice=int(input("enter Your choice:"))
if choice==1:
    num=int(input("enter any no:"))
    sum=0
    i=1

    while i<num:     
        if num%i==0:  
            sum+=i
        i+=1

    if num==sum:
        print("Perfect no")
    else:
        print("Not perfect no")
        

elif choice==2:
    num=int(input("Enter any no:"))
    rev=0
    temp=num

    while num>0:
        rem=num%10
        rev=(rev*10)+rem
        num//=10

    if rev==temp:
        print("No is palindrome")
    else:
        print("No is not palindrome")
    
        

elif choice==3:
    num=int(input("enter any no:"))
    i=1
    fact=1
    while i<=num:
        fact*=i
        i+=1

    print("Factorial of 5:",fact)
    

elif choice==4:
    num=int(input("enter any no:"))
    sum=0
    product=1

    while num>0:               
        rem=num%10             
        sum=sum+rem            
        product=product*rem   
        num=num//10            

    if sum==product:
        print("No is spy")
    else:
        print("No is not spy")


elif choice==5:
    num=int(input("Enter any no:"))
    square=num**2       # 9**2=81
    sum=0
    while square>0:        #81>0  1>0 
        digit=square%10    # 8 1 
        sum+=digit         #8+0=8  8+1=9
        square//=10        # 1 0

    if sum==num:
        print("it is neon no")
    else:
        print("It is not neon no")

elif choice==6 :
    print("Thank you!")

else:
    print("Invalid ip")




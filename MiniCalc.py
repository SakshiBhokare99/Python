ip=int(input("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Power\n6.Exit\n"))
num1=int(input("Enter no 1 : "))
num2=int(input("Enter no 2 : "))

if ip==1:
    print("Addition is :",num1+num2)
elif ip==2:
    print("Subtraction is :",num1-num2)
elif ip==3:
    if num1>0 and num2>0:
      print("Multiplication is : ", num1*num2)
    else:
       print("dont multiply by 0")
elif ip==4:
    if num1>0 and num2>0:
      print("Division is : ",num1/num2)
    else:
        print("dont divide by 0")
elif ip==5:
    print("Power is : ",num1**num2)
elif ip==6:
    print("Exit")
else:
    print("Invalid input")
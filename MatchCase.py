# 1-5 --> weekdays  , 6-7 --> weekend , invalid ip
# ip=int(input("Enter no to check day(1-7)"))
# match ip:
#     case 1: print("Monday weekday")
#     case 2: print("Tuesday weekday")
#     case 3:print("Wednesday weekday")
#     case 4:print("Thursday weekday")
#     case 5:print("Friday weekday")
#     case 6:print("Saturday weekend")
#     case 7:print("Sunday weekend")
 

# match ip:
#     case 1 | 2 | 3 | 4 | 5: print("Weekday")
#     case 6 | 7:print("weekend")
#     case _ : print("Invalid ip")

#check no with month
'''ip=int(input("Enter no to check month"))
match ip:
    case 1 | 2 | 3 | 4 | 5 if ip==1 : print("Jan")
    case 1 | 2 | 3 | 4 | 5 if ip==2 : print("Feb")
    case 1 | 2 | 3 | 4 | 5 if ip==3 : print("Mar")
    case 1 | 2 | 3 | 4 | 5 if ip==4 : print("Apr")
    case 1 | 2 | 3 | 4 | 5 if ip==5 : print("May")'''

# payment : card / upi / cash/
# card -> 10% extra gst , upi->enter upi id , cash->cash in delivery available
payment=input("Payment modes are : cash / UPI / Card\n")
match payment:
    case "cash":print("Cash on delivery is available")
    case "UPI":print("Enter your UPI Id")
    case "Card":print("On card 10 % gst included")
    case _:print("Other payment mode is not available")


   
    
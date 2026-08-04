# Print 1 to 50 
# No is %3 - >cube -> sum
# No is %9 -> square -> sum
# No is %2 and 4% -> no^6 


num=1
Csum=0
Ssum=0

while num<=50:
    if num%3==0:
        cube=num**3
        Csum+=cube
        print("Number:",num,"Cube:",cube,"Cube sum:",Csum)
    
    if num%9==0:
        square=num**2
        Ssum+=square
        print("Number:",num,"Square:",square,"Square sum:",Ssum)

    if num%2==0 and num%4==0:
        power=num**6
        print("Number:",num,"Power",power)
    num+=1
print("Cube Sum:",Csum)
print("Square sum:",Ssum)
    

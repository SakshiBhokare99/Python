# Sad no: no that eventually become 4 when replace by sum of square of its digit repeatedly
# Ex : No=3
#3**2=9 9**2=81 64+1=65 = 36+25=61 36+1=37  9+49=58 = 25+64=89 = 64+25=145 = 1+16+25=42 
# 16+4=20 2**2=4

num = int(input("Enter a number: "))

original = num
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** 2
        num //= 10

    num = total

if num == 1:
    print(original, "is a Happy Number")
else:
    print(original, "is a Sad Number")
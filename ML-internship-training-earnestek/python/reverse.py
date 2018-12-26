def reverse(num):
    rev = 0
    while(num > 0):
        r = num % 10
        rev = (rev * 10) + r
        num = num // 10
    return rev
    
number = int(input("enter a number: "))

print(f"{number} when reversed is {reverse(number)}")
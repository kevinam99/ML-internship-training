def factorial(num):
    if num == 1:
        return 1
    else:
        return num  * factorial(num-1)
       # num = num * factorial(num - 1)
    #return num

num = int(input("Enter a number: "))
print(factorial(num))


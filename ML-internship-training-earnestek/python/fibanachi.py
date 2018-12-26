def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the number of terms: "))
for i in range(1, n+1):
    print(f"{i}. {fibo(i)}")
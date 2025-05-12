def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

print(facto(5))


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)
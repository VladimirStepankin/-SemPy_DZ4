def fun(x, n):
    if n == 0:
        return 1
    return x * fun(x, n-1)
a = int(input())
b = int(input())
print(fun(a, b))
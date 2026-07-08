def f(n, k):
    if n == k:
        return 1
    elif n < k:
        return 0
    else:
        return f(n - 1, k) + f(n - 3, k) + f(n // 2, k)

print(f(31, 3) - f(31, 20) * f(20, 8) * f(8, 3))

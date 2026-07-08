def f(n, k):
    if n == k:
        return 1
    elif n > k or n == 17 or n == 28:
        return 0
    else:
        return f(n + 2, k) + f(n + 3, k) + f(n * 2, k)

print(f(8, 14)*f(14, 48) + f(8, 18) * f(18, 48) - f(8, 14)*f(14, 18)*f(18, 48))

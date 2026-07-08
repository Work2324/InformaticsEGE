def f(n, k):
    if n == k:
        return 1
    elif n > k:
        return 0
    else:
        return f(n + 1, k) + f(n * 2, k) + f(n * 2 + 1, k) + f(n * 10, k)

print(f(1, 15))

def fun(n, k):
    if n == k:
        return 1
    elif n < k:
        return 0
    else:
        return fun(n - 3, k) + fun(n // 2, k)

print(5 // 2, 8//3)
print(fun(73, 13)*fun(13, 2))

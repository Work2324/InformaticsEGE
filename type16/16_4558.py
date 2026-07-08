def f(n):
    if n == 1:
        return 1;
    elif n > 1:
        return f(n-1) * n
    else: #не обязательно, но желательно
        print("error")
        return 0

print(f(5))

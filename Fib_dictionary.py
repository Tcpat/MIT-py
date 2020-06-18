def fib_dict(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_dict(n-1, d) + fib_dict(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_dict(1033, d))

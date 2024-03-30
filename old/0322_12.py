def for_loop(n):
    if n == 1:
        return 1
    return n + for_loop(n - 1)

print(for_loop(10))
def fib_memo(num, cache={}):
    if num in cache:
        return cache[num]
    if num == 0:
        return 0
    if num == 1:
        return 1
    cache[num] = fib_memo(num - 1, cache) + fib_memo(num - 2, cache)
    return cache[num]

def fib_tab(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    fib = [0] * (num + 1)
    fib[0] = 0
    fib[1] = 1

    for index in range(2, num + 1):
        fib[index] = fib[index - 1] + fib[index - 2]

    return fib[num]

n = int(input("Enter the position (n): "))

print("Using Memoization:", fib_memo(n))
print("Using Tabulation:", fib_tab(n))
"""
generate nth fibonacci term
"""
from duration import duration
from multiprocessing import Process


def fib_recursion(n):
    # using recursion
    if n == 0: return 0
    if n == 1: return 1
    return fib_recursion(n-1) + fib_recursion(n-2)


def cache_fib(n, r):
    # memoization
    if r[n] >= 0:
       return r[n]
    if n == 0 or n == 1:
        num = n
    else:
        num = cache_fib(n-1, r) + cache_fib(n-2, r)
    r[n] = num
    return num

@duration
def fib_dynamic_programming(n):
    # using dp
    r = [-1]*(n+1)
    return cache_fib(n, r)

@duration
def func(num):
    return fib_recursion(num)

@duration
def fib_simple(num):
    if num == 0:return 0
    a = 0
    b = 1
    for i in range(num):
        c = a + b
        a = b
        b = c
    return a+b


if __name__ == '__main__':
    p1 = Process(target=func, args=(20,))
    p1.start()
    p2 = Process(target=fib_dynamic_programming, args=(20,))
    p2.start()
    p3 = Process(target=fib_simple, args=(20,))
    p3.start()
    p1.join()
    p2.join()
    p3.join()





import memoization_thetheos as mem

if mem.fib_it(9) == 34:
    print("Test 1 Ok")
if mem.fib_it_cul(9) == 34:
    print("Test 2 Ok")
if mem.fib_rec(9) == 34:
    print("Test 3 Ok")
if mem.fibo_mem(9) == 34:
    print("Test 4 Ok")
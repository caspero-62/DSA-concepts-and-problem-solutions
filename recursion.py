# Fibonacci sequence using recursion

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    return get_fib(position-1) + get_fib(position-2)
    

def print_fib_series(position):
    fib_sequence = []
    while position >= 0:
        fib_sequence.insert(0, get_fib(position))
        position -= 1
    return fib_sequence

print(print_fib_series(9))
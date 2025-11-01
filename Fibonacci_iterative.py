#Fibonnaci series: Iterative solution
"""
Always handle errors like a non-negative input.
It offers O(n) time and O(1) space compexity. It is efficient than a recursive solution.
"""
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be non-negative number")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (b+a)
    return a

for x in range(5):
    print(f"F{x}: {fib(x)}")

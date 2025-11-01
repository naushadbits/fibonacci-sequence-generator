#Fibonacci Recursive Solution
"""
    Return the nth Fibonacci number using recursion.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    
    Time Complexity is O(2^n) because each call branches into two.
    Space Complexity is O(n) due to recursion stack depth.
"""
def fib(n:int)->int:    
    if n <= 0:
        return 0
    if n<=1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(5):
    print(f"F{i}: {fib(i)}")



import sys

# ── Non-Recursive (Iterative) ──────────────────────────────
# Time Complexity : O(n)  - single loop runs n times
# Space Complexity: O(1)  - only two variables used
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    # Build up the answer one step at a time
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# ── Recursive ──────────────────────────────────────────────
# Time Complexity : O(2^n) - each call branches into two recursive calls
# Space Complexity: O(n)   - call stack depth goes up to n
def fibonacci_recursive(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Each call breaks the problem into two smaller subproblems
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# ── Driver ─────────────────────────────────────────────────
if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    n = int(input("Enter n: "))

    print(f"Iterative  -> F({n}) = {fibonacci_iterative(n)}")
    print(f"Recursive  -> F({n}) = {fibonacci_recursive(n)}")

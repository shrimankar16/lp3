# 0-1 Knapsack Problem - Dynamic Programming
#
# Each item is either taken (1) or not taken (0) — no fractions allowed.
#
# Approach: Build a 2D DP table where dp[i][w] = max value using
#           first i items with capacity w.
#
# Time Complexity : O(n * W) - fill an n x W table
# Space Complexity: O(n * W) - the DP table

def knapsack_dp(capacity, weights, values, n):
    # Create DP table of size (n+1) x (capacity+1), initialized to 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]

            # Take item i (only if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp


def find_selected_items(dp, weights, values, n, capacity):
    # Traceback through DP table to find which items were selected
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        # If value changed from row above, item i was included
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    return selected[::-1]   # reverse to get original order


# ── Driver ────────────────────────────────────────────────
if __name__ == "__main__":
    n = int(input("Enter number of items: "))

    weights = []
    values  = []

    for i in range(n):
        w, v = map(int, input(f"  Item {i+1} - Enter weight and value: ").split())
        weights.append(w)
        values.append(v)

    capacity = int(input("Enter knapsack capacity: "))

    dp       = knapsack_dp(capacity, weights, values, n)
    max_val  = dp[n][capacity]
    selected = find_selected_items(dp, weights, values, n, capacity)

    print("\nSelected Items:")
    print(f"  {'Item':<8} {'Weight':<10} {'Value'}")
    print("  " + "-" * 28)
    for idx in selected:
        print(f"  {idx:<8} {weights[idx-1]:<10} {values[idx-1]}")

    print(f"\nMaximum Value : {max_val}")

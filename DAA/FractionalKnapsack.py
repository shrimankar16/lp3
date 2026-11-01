# Fractional Knapsack Problem - Greedy Method
#
# Greedy choice: pick items with the highest value/weight ratio first.
#                If an item doesn't fit fully, take the fraction that fits.
#
# Time Complexity : O(n log n) - sorting items by ratio
# Space Complexity: O(n)       - storing items

def fractional_knapsack(capacity, items):
    # Calculate value/weight ratio for each item and sort in descending order
    # items = list of (weight, value)
    items_with_ratio = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    total_value  = 0.0
    result       = []   # stores (item_index, weight_taken, value_gained)

    for i, (weight, value) in enumerate(items_with_ratio):
        if capacity == 0:
            break

        # Take the full item if it fits
        if weight <= capacity:
            total_value += value
            capacity    -= weight
            result.append((i + 1, weight, value))

        else:
            # Take only the fraction that fits
            fraction     = capacity / weight
            total_value += value * fraction
            result.append((i + 1, round(capacity, 2), round(value * fraction, 2)))
            capacity     = 0

    return total_value, result


# ── Driver ────────────────────────────────────────────────
if __name__ == "__main__":
    n        = int(input("Enter number of items: "))
    items    = []

    for i in range(n):
        w, v = map(float, input(f"  Item {i+1} - Enter weight and value: ").split())
        items.append((w, v))

    capacity = float(input("Enter knapsack capacity: "))

    total_value, selected = fractional_knapsack(capacity, items)

    print("\nSelected Items:")
    print(f"  {'Item':<8} {'Weight Taken':<16} {'Value Gained'}")
    print("  " + "-" * 38)
    for item_no, wt, val in selected:
        print(f"  {item_no:<8} {wt:<16} {val}")

    print(f"\nTotal Value in Knapsack: {total_value:.2f}")

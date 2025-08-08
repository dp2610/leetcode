from typing import List


def getMaximumGrossValue(arr: List[int]) -> int:
    """Return the maximum gross value for any valid triplet.

    The gross value for 1-based indices (i1, i2, i3) is defined using half-open sums:
      sum(l, r) includes l and excludes r. Empty sums are 0.

    This implementation runs in O(n) time and O(n) space.
    """
    n = len(arr)
    if n == 0:
        return 0

    total = sum(arr)

    # bestSuffix[i] = maximum subarray sum within arr[i..n-1], allowing empty (0)
    best_suffix = [0] * (n + 1)
    # bestStartingHere helper to compute subarray starting exactly at i
    best_starting_here = 0
    max_start_array = [0] * (n + 1)

    # Build from right to left
    for i in range(n - 1, -1, -1):
        best_starting_here = max(arr[i], arr[i] + best_starting_here)
        max_start_array[i] = best_starting_here
        best_suffix[i] = max(0, max(max_start_array[i], best_suffix[i + 1]))

    prefix = 0  # sum(1, i1) with i1 starting at 1 maps to prefix at i1_index = 0
    best = float("-inf")
    for i1_index in range(0, n + 1):  # i1_index corresponds to i1-1 in 0-based
        best = max(best, prefix + best_suffix[i1_index])
        if i1_index < n:
            prefix += arr[i1_index]

    return 2 * best - total


if __name__ == "__main__":
    example = [-5, 3, 9, 4]
    print(getMaximumGrossValue(example))  # Expected: 21
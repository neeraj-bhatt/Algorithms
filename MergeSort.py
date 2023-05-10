import random
import time
import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_comparisons = merge_sort(arr[:mid])
    right, right_comparisons = merge_sort(arr[mid:])
    merged, merge_comparisons = merge(left, right)

    return merged, left_comparisons + right_comparisons + merge_comparisons

def merge(left, right):
    i = j = comparisons = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        comparisons += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, comparisons

def test_merge_sort():
    num_tests = 100
    min_size = 30
    max_size = 100
    total_comparisons = [0] * (max_size - min_size + 1)
    for i in range(num_tests):
        size = random.randint(min_size, max_size)
        arr = [random.randint(1, 1000) for _ in range(size)]
        _, num_comparisons = merge_sort(arr)
        total_comparisons[size - min_size] += num_comparisons
    avg_comparisons = [count / num_tests for count in total_comparisons]
    return avg_comparisons

# Test merge sort and report the average number of comparisons for each input size
avg_comparisons = test_merge_sort()
for i, count in enumerate(avg_comparisons):
    print(f"Input size {i+30}: Average number of comparisons = {count:.2f}")

# Generate graph of the average number of comparisons made by merge sort
plt.plot(range(30, 101), avg_comparisons, label="Merge sort")

# Generate graph of expected number of comparisons (proportional to n log n)
nlogn = [n * np.log2(n) for n in range(30, 101)]
plt.plot(range(30, 101), nlogn, label="n log n")

plt.xlabel("Input size")
plt.ylabel("Number of comparisons")
plt.legend()
plt.show()

import random
import math
import matplotlib.pyplot as plt

def randomized_quicksort(arr, lo, hi):
    if lo < hi:
        comparisons = 0
        p, comparisons = randomized_partition(arr, lo, hi)
        comparisons += randomized_quicksort(arr, lo, p-1)
        comparisons += randomized_quicksort(arr, p+1, hi)
        return comparisons
    else:
        return 0

def randomized_partition(arr, lo, hi):
    i = random.randint(lo, hi)
    arr[i], arr[hi] = arr[hi], arr[i]
    return partition(arr, lo, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    comparisons = 0
    for j in range(lo, hi):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1, comparisons

def generate_random_array(size):
    return [random.randint(-1000, 1000) for _ in range(size)]

def theoretical_comparisons(n):
    return n * math.log(n, 2)

def plot_results(sizes, actual_comparisons):
    theoretical = [theoretical_comparisons(size) for size in sizes]
    plt.plot(sizes, actual_comparisons, label="Randomized Quicksort")
    plt.plot(sizes, theoretical, label="Theoretical")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Number of Comparisons")
    plt.legend()
    plt.show()

sizes = list(range(30, 101))
actual_comparisons = []
for size in sizes:
    total_comparisons = 0
    for i in range(100):
        arr = generate_random_array(size)
        comparisons = randomized_quicksort(arr, 0, len(arr)-1)
        total_comparisons += comparisons
    actual_comparisons.append(total_comparisons / 100)
plot_results(sizes, actual_comparisons)

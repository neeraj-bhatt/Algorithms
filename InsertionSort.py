import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return arr, comparisons

def test_insertion_sort():
    num_tests = 100
    min_size = 30
    max_size = 100
    total_comparisons = [0] * (max_size - min_size + 1)
    for i in range(num_tests):
        size = random.randint(min_size, max_size)
        arr = [random.randint(1, 1000) for _ in range(size)]
        _, num_comparisons = insertion_sort(arr)
        total_comparisons[size - min_size] += num_comparisons
    avg_comparisons = [count / num_tests for count in total_comparisons]
    return avg_comparisons

def nlogn(size):
    return size * (size - 1) / 2 * (2 / size)

sizes = list(range(30, 101))
avg_comparisons = test_insertion_sort()
nlogn_values = [nlogn(size) for size in sizes]

plt.plot(sizes, avg_comparisons, label="Insertion Sort")
plt.plot(sizes, nlogn_values, label="nlogn")
plt.xlabel("Input size")
plt.ylabel("Number of comparisons")
plt.title("Insertion Sort vs nlogn")
plt.legend()
plt.show()

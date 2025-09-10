import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Розміри масивів
sizes = [100, 1000, 5000, 10000]

# Заголовок таблиці
print("=" * 70)
print(f"{'Розмір':<12}{'Insertion Sort':<20}{'Merge Sort':<20}{'Timsort':<15}")
print("=" * 70)

# Тестування та вивід
for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

    print(f"{size:<12}{insertion_time:<20.6f}{merge_time:<20.6f}{timsort_time:<15.6f}")

print("=" * 70)
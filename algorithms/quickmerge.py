import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def generate_random_list(n):
    return [random.randint(1, 1000) for _ in range(n)]

if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    
    random_list = generate_random_list(n)
    
    # Measure time for quick sort
    quick_start_time = time.time()
    quick_sort(random_list.copy())
    quick_end_time = time.time()
    quick_time = quick_end_time - quick_start_time

    # Measure time for merge sort
    merge_start_time = time.time()
    merge_sort(random_list.copy())
    merge_end_time = time.time()
    merge_time = merge_end_time - merge_start_time

    # Display the results
    print(f"\nTime taken for Quick Sort: {quick_time:.6f} seconds")
    print(f"Time taken for Merge Sort: {merge_time:.6f} seconds")

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_random_list(n):
    return [random.randint(1, 1000) for _ in range(n)]

if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    
    random_list = generate_random_list(n)

    bubble_start_time = time.time()
    bubble_sort(random_list.copy())
    bubble_end_time = time.time()
    bubble_time = bubble_end_time - bubble_start_time

    insertion_start_time = time.time()
    insertion_sort(random_list.copy())
    insertion_end_time = time.time()
    insertion_time = insertion_end_time - insertion_start_time


    print(f"\nTime taken for Bubble Sort: {bubble_time:.6f} seconds")
    print(f"Time taken for Insertion Sort: {insertion_time:.6f} seconds")

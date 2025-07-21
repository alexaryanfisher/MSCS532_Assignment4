"""
Assignment 4: Comparison, Part 1 section 3.

This is a comparison implementation for Heapsort, Quicksort, and Mergesort based on running time and input sizes.

"""
from Heapsort import heapsort
import random
import time
import sys

# Increase the recursion limit to handle larger inputs.
sys.setrecursionlimit(20000)

# Mergesort implementation
def mergesort(arr):
    if len(arr) <= 1:
        #List is already sorted.
        return arr
    
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])

    # Recursively sort both halves.
    left_half = mergesort(left_half)
    right_half = mergesort(right_half) 

    # Merge the sorted halves.
    return merge(left_half, right_half)

# Merge function to combine two sorted lists.
def merge(left, right):
    merged_list = []
    # Initialize pointers for both lists.
    # Pointer for left list.
    i = 0
    #Pointer for right list.
    j = 0

    # Merge the two lists while maintaining order.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # Append any remaining elements.
    while i < len(left):
        merged_list.append(left[i])
        i += 1
    while j < len(right):
        merged_list.append(right[j])
        j += 1
    return merged_list

# Quicksort implementation (Using random pivot selection for better performance on average)
def quicksort(arr):
    # Call recursive helper function.
    _quicksort_helper(arr, 0, len(arr) - 1)
    return arr

def _quicksort_helper(arr, low, high):
    if low < high:
        # Partition the array and get the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        _quicksort_helper(arr, low, pi - 1)
        _quicksort_helper(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose random pivot element
    random_pivot_index = random.randint(low, high)
    arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]

    #Set to random pivot element
    pivot = arr[high]
    i = (low - 1)  # Pointer for the smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at i + 1 to place it in the correct position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Data Generation functions to provide different input sizes for testing.

# Generate a random list of integers.
def generate_random_list(size, max_value=10000):
    return [random.randint(1, max_value) for _ in range(size)]

# Generate already sorted list.
def generate_sorted_list(size):
    return list(range(1, size + 1))

# Generate a list sorted in reverse order.
def generate_reverse_sorted_list(size):
    return list(range(size, 0, -1))

# Comparsion function to compare the performance of sorting algorithms.
def comparison_analysis(array_type, size):
    if array_type == 'random':
        original_arr = generate_random_list(size)
    elif array_type == 'sorted':
        original_arr = generate_sorted_list(size)
    elif array_type == "reverse_sorted":
        original_arr = generate_reverse_sorted_list(size)
    else:
        # Error checking.
        raise ValueError ("Invalid array type.")
    
    # Running Time functions

    # Time Measurement of Heapsort
    arr_heap = list(original_arr)
    start_time_heap = time.perf_counter()
    heapsort(arr_heap)
    end_time_heap = time.perf_counter()
    # Elapsed time in seconds
    elapsed_time_heap = end_time_heap - start_time_heap
    # Converts to milliseconds
    elapsed_time_heap_ms = elapsed_time_heap * 1000
    

    # Time Measurement of Mergesort
    arr_merge = list(original_arr)
    start_time_merge = time.perf_counter()
    mergesort(arr_merge)
    end_time_merge = time.perf_counter()
    # Elapsed time in seconds
    elapsed_time_merge = end_time_merge - start_time_merge
    # Converts to milliseconds
    elapsed_time_merge_ms = elapsed_time_merge * 1000

    # Time Measurement of Quicksort (Random)
    arr_quick = list(original_arr)
    start_time_quick = time.perf_counter()
    quicksort(arr_quick)
    end_time_quick = time.perf_counter()
    # Elapsed time in seconds
    elapsed_time_quick = end_time_quick - start_time_quick
    # Converts to milliseconds
    elapsed_time_quick_ms = elapsed_time_quick * 1000

    print(f"Array Type: {array_type}, Size: {size}")
    print(f"Heapsort Execution Time: {elapsed_time_heap_ms} ms.")
    print(f"Mergesort Execution Time: {elapsed_time_merge_ms} ms.")
    print(f"Quicksort (Randomized) Execution Time: {elapsed_time_quick_ms} ms.")

# Main Execution for Comparsion.

if __name__ == "__main__":
    print("Sorting Algorithm Performance Comparison testing starting.")

    # Various input sizes to test.
    sizes = [100, 1000, 5000, 10000, 15000]

    for size in sizes:
        # Print size being tested
        print(f"\n Testing with Size: {size}")
        #  Complete comparisons for different algorithms, array types, and noted sizes.
        comparison_analysis("random", size)
        comparison_analysis("sorted", size)
        comparison_analysis("reverse_sorted", size)
    # Comfirming testing is completed.
        print ("\n Comparsion testing completed.\n")
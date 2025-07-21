"""
Assignment 4: Heapsort, Part 1

Heap Sort implementation in Python.
This is an implementation of the heapsort algorithm showcasing the correct steps for building a max-heap, extracting meximum element, and maintaining the heap property.

"""
import random
import time


# Define heapify function that maintains the max-heap property for subtree rooted at index "i". 
# arr is the list representing the heap.
# n is the size of the heap.
# i is the index of the element to heapify.
# Reference: https://www.geeksforgeeks.org/heap-sort/

def heapify(arr, n, i):
    # Intialize largest as root
    largest = i
    # Index of left child of root.
    l = 2 * i + 1
    # Index of right child root.
    r = 2 * i + 2

    # If left child exists and is greater than root. Set the largest to left child.
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    # If right child exists and is greater than the current largest. Set the largest to right child.
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root, swap root with largest and continue heapifying the affected subtree.
    if largest != i:
        #Swap
        arr[i], arr[largest] = arr[largest], arr[i]
        #Recursively heapify the affected subtree
        heapify(arr, n, largest)

# Function to build a max-heap from the given array. This is the first step in heapsort.
def max_heap(arr):
    n = len(arr)
    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Function to perform heapsort on the array.
def heapsort(arr):
    if len(arr) <= 1:
        #Already sorted.
        return
    
    n = len(arr)

    # Step 1: Build a max-heap from the array.
    max_heap(arr)

    # Step 2: Extract elements from the heap one by one.
    for i in range(n - 1, 0, -1):
        # Move current root to the end of the array.
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap.
        heapify(arr, i, 0)

# Use Cases
if __name__ == "__main__":
    print("Use Cases for Heapsort.")

    # Use Case 1: Sorting an unsorted array
    print("\n Use Case: Unsorted Array")
    arr1 = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr1)
    heapsort(arr1)
    print("Sorted array:", arr1)

    # Use Case 2: Sorting an already sorted array
    print("\n Use Case: Already Sorted Array")
    arr2 = [1, 2, 3, 4, 5]
    print("Original array:", arr2)
    heapsort(arr2)
    print("Sorted array:", arr2)

    # Use Case 3: Sorting an array with duplicate elements
    print("\n Use Case: Array with Duplicates")
    arr3 = [3, 1, 2, 3, 1, 2]
    print("Original array:", arr3)
    heapsort(arr3)
    print("Sorted array:", arr3)

    # Use Case 4: Sorting an empty array
    print("\n Use Case: Empty Array")
    arr4 = []
    print("Original array:", arr4)
    heapsort(arr4)
    print("Sorted array:", arr4)

    # Use Case 5: Sorting  a reverse sorted array
    print("\n Use Case: Reverse Sorted Array")
    arr5 = [5, 4, 3, 2, 1]
    print("Original array:", arr5)
    heapsort(arr5)
    print("Sorted array:", arr5)

    # Use Case 6: Sorting a large array, for performance observation.
    print("\n Use Case: Large Array")
    arr6 = [random.randint(1, 1000) for _ in range(100)]
    print("Original array (first 15 elements):", arr6[:15])
    heapsort(arr6)
    print("Sorted array (first 15 elements):", arr6[:15])
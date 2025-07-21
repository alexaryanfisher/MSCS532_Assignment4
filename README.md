# Heap Data Structures; Implementation, Analysis, Applications

This repository contains my fourth assignment for MSCS532. This is an Python implementation of Heapsort and a Priority Queue Task application.

## Project Overview
The assignment aims to show the understanding of heap data structures and their implementation using arrays along with their applications in sorting and priority queue operations. 

 * ### Part 1: Heapsort Implementation
      This part of the implementations highlights the heapsort algorithm and provides an empirical comparsion between Heapsort, Quicksort, and Mergesort. The comparison was conducted on different input sizes and distributions such as randomly generated arrays, already sorted arrays, and reverse-sorted arrays.

 * ### Part 2: Priority Queue Implementation
      This part of the project implements the use of a binary heap using a Python list (array), class structures, and max heap type.

## Project Deliverables:
```Heapsort.py``` : Python file containing implementation of heapsort algorithm along with use cases.

```Comparison.py``` : Python file containing implementation of heapsort, mergesort, and quicksort(random pivot) algorithms to provide a comparsion on running time performance.

```PriorityQueue.py``` : Python file that implements a priority queue data structure and core heap operations.

```ProjectReport.md```: Report containing Heapsort analysis of time complexity, <em>O(n</em>log<em> n)</em> explanation, and space complexity. It also contains Priority Queue design choices, implementation details and analysis of scheduling results. [Pending]

## Summary of Findings
This project’s empirical application and theoretical analysis provide insight into the efficient	 and practical usage of heap data structures for sorting and priority applications. Heapsort consistently represented a <em>O(n </em>log <em> n)</em> performance across all input arrays such as random, sorted, and reverse sorted. Quicksort with a random pivot did showcase a faster execution time due to constant factors and cache locality, heapsort did provide predictable performance without the risk <em>On^2</em> worst case scenarios found in other quicksort implementations.  This makes it a reliable choice overall.

The Priority Queue implementation validated the expected time complexities of its core operations of ```insert ```,  ``` extractmax ``` , and ``` modify ``` by performing in <em>O(</em>log <em> n)</em> time. The array based max heap underscore the reliability of heap-based priority queues can reinforce the value heap data structures bring.


### How to Run Code
* Clone the repository or save all Python files into a folder.
* Open terminal or preferred IDE.
* Navigate and open the save file.
* Run the scripts using a Python interpreter.

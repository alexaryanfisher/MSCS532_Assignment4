# Project Report 
### by Alexa Fisher

[Pending]

## Analysis of Heapsort
### Time Complexity Analysis
Heapsort is a comparison-based sorting algorithm that achieves a time complexity of <em> O(n</em> log<em> n)</em> consistently across all cases of worst, average, and best. In heapsort, the algorithm has two phases of building a max-heap and extracting elements. This initial phase of building the max-heap transforms the input array into a max-heap, where the largest element is at the root. It is achieved by iterating from the last non-leaf node to the root and applying the heapify procedure to each subtree. The heapify operation restores the heap property by bubbling down an element (Cormen et al, 2022). This recursive process takes <em> O(</em> log<em> k)</em> time for a subtree of size <em>k</em>. After the max-heap is built, the largest element is swapped with the last element of the array. The heap’s size is effectively reduced by 1  (Chen et al, 2018). The heapify process is then called on the new root and repeated <em>n – 1</em> times (Chen et al, 2018). The total cost of this phase is 
![totaltime](https://github.com/alexaryanfisher/MSCS532_Assignment4/blob/main/images/totaltime.png) . When you combine both of these phases, <em> O(n)</em> + <em> O(n</em> log<em> n)</em> = <em> O(n</em> log<em> n)</em>. This holds true for all scenarios because the algorithm's processes are deterministic and perform the same number of steps regardless of the initial order of the elements in the array (Chen et al, 2018).

### Space Complexity
Heapsort is an in-place sorting algorithm. Its space complexity is <em>O(1) </em>. Additional memory space is only needed in addition to the input array (Cormen et al, 2022). The heapsort algorithm can increase its speed of sorting without taking up any additional memory space (Chen et al, 2018).

### Comparsion Observations
The comparison provided by the empirical application highlighted a distinct performance observation for heapsort, mergesort, and quicksort (random pivot) algorithms. Each of these aligned with their theoretical time complexities. The observation can be reviewed in Figure 1 below.
The quicksort with a random pivot consistently showed fast execution time across all array types and sizes. It validates its <em> O(n</em> log<em> n)</em> average-case time efficiency. The mergesort showed significantly higher execution times across all array types and sizes. Although it has a theoretical time complexity of <em> O(n</em> log<em> n)</em>, it is highly impacted by larger constant factors due to overhead during the merge step. The heapsort mirrored quicksort with random pivot’s consistency across all the array type and sizes as expected based on its theoretical analysis. Whereas, its execution time was slightly higher in comparison to quicksort(random pivot).

<strong> Figure 1</strong>
<br>
<strong><em>Heapsort, Mergesort, Quicksort(Random Pivot Comparsion Results)</em></strong>

    Sorting Algorithm Performance Comparison testing starting.

    Testing with Size: 100
    Array Type: random, Size: 100
    Heapsort Execution Time: 0.09780004620552063 ms.
    Mergesort Execution Time: 2.026899950578809 ms.
    Quicksort (Randomized) Execution Time: 0.07670000195503235 ms.
    Array Type: sorted, Size: 100
    Heapsort Execution Time: 0.08780008647590876 ms.
    Mergesort Execution Time: 1.6467999666929245 ms.
    Quicksort (Randomized) Execution Time: 0.05679996684193611 ms.
    Array Type: reverse_sorted, Size: 100
    Heapsort Execution Time: 0.14399993233382702 ms.
    Mergesort Execution Time: 3.3732999581843615 ms.
    Quicksort (Randomized) Execution Time: 0.06870005745440722 ms.

    Comparsion testing completed.


    Testing with Size: 1000
    Array Type: random, Size: 1000
    Heapsort Execution Time: 3.3085999311879277 ms.
    Mergesort Execution Time: 154.47900001890957 ms.
    Quicksort (Randomized) Execution Time: 0.7334999972954392 ms.
    Array Type: sorted, Size: 1000
    Heapsort Execution Time: 1.304800040088594 ms.
    Mergesort Execution Time: 152.0521999336779 ms.
    Quicksort (Randomized) Execution Time: 0.6929000373929739 ms.
    Array Type: reverse_sorted, Size: 1000
    Heapsort Execution Time: 1.1192000238224864 ms.
    Mergesort Execution Time: 149.19680007733405 ms.
    Quicksort (Randomized) Execution Time: 1.018799957819283 ms.

    Comparsion testing completed.


    Testing with Size: 5000
    Array Type: random, Size: 5000
    Heapsort Execution Time: 8.29079991672188 ms.
    Mergesort Execution Time: 4225.501300068572 ms.
    Quicksort (Randomized) Execution Time: 4.416299983859062 ms.
    Array Type: sorted, Size: 5000
    Heapsort Execution Time: 9.613899979740381 ms.
    Mergesort Execution Time: 4342.325600096956 ms.
    Quicksort (Randomized) Execution Time: 3.895399975590408 ms.
    Array Type: reverse_sorted, Size: 5000
    Heapsort Execution Time: 8.314500097185373 ms.
    Mergesort Execution Time: 4107.691599987447 ms.
    Quicksort (Randomized) Execution Time: 4.28330001886934 ms.

    Comparsion testing completed.


    Testing with Size: 10000
    Array Type: random, Size: 10000
    Heapsort Execution Time: 17.461600014939904 ms.
    Mergesort Execution Time: 16351.273900014348 ms.
    Quicksort (Randomized) Execution Time: 9.208500036038458 ms.
    Array Type: sorted, Size: 10000
    Heapsort Execution Time: 19.737199996598065 ms.
    Mergesort Execution Time: 16156.421800027601 ms.
    Quicksort (Randomized) Execution Time: 8.182000019587576 ms.
    Array Type: reverse_sorted, Size: 10000
    Heapsort Execution Time: 15.591899980790913 ms.
    Mergesort Execution Time: 16331.783500034362 ms.
    Quicksort (Randomized) Execution Time: 11.364200036041439 ms.

    Comparsion testing completed.


    Testing with Size: 15000
    Array Type: random, Size: 15000
    Heapsort Execution Time: 29.247500002384186 ms.
    Mergesort Execution Time: 34340.86939995177 ms.
    Quicksort (Randomized) Execution Time: 14.368099975399673 ms.

    Comparsion testing completed.


## Priority Queue Implementation
### Design Choice
The application implemented the Priority Queue data structure in Python for tasks to be processed based on urgency. The core design is a binary heap. This array based binary heap uses a max heap to ensure that tasks with the highest priority are noted first.
The use of a list was chosen to represent the binary heap. It was justified due to its simplicity and efficiency in heap operations.  The mapping of the binary tree to an array was calculated into parent, left child, and right child. The calculation removed the need for explicit pointers, which provided a cache-friendly memory.
A Task class was defined to represent the scheduling units and each task included the task_id, priority, arrival_time, deadline, and description.  The heap type was max-heap. It was implemented because it prioritized task with the highest urgency first. This enables the access time to be <em>O(1)</em> for the most critical task constantly.  

### Time Complexity Analysis of Core Operations
The logic and time complexity for each of the core operations can be found in the below chart.

<strong>Chart 1</strong>
<br>
<strong><em>Core Operations Chart: Logic and Time Complexity</em></strong>
<br>
| Core Operation |   Logic   | Time Complexity |
|--------------- | --------- | --------------- |
| ```insert(task)``` |  A new task is appended to the end of the ```_heap``` list. Its  index in the heap and its task id to the index mapping is updated. The function ``` headify_incr``` ( bubble up) is called on the new task's position. The process repeatedly compares the task with its parent and swaps then if the child has a higher priority. This moves it up in the heap until the max-heap property is restored. | <em>O(</em> log <em>n)</em>|
|```extractmax()``` | It retrieves and removed the highest priority task which is the root element. If the heap is not empty the root is stored and the last element is moved to the root's position in the heap. The last element is then removed from the list. The task id to index mapping is updated and the ```_heapify_desc```(bubble down) is called on the new root. The process repeatedly compares the task with its parent and swaps then if the child has a higher priority. This moves it down in the heap until the max-heap property is restored. | <em>O(</em> log <em>n)</em>|
|``` modify(task_id, new_priority)``` | The modify method changes the existing task's priority. It uses the task id to index diction to find the task's current index. After updating the task priority, it calls the ```heapify_incr``` or ```heapify_decr``` to restore dependent on if the new priority is greater or less than the old priority. | <em>O(</em> log <em>n)</em>|
| ``` isempty()``` | Checks if the heap list is empty | <em>O(1)</em>|
| ```peekmax()``` | Displays the task id of the highest priority task, the root, without removing it. | <em>O(1)</em>|

### Analysis of Scheduling Results
The provided main block serves as a demonstration of the Priority Queue's functionality. It simulates the basic task scheduling scenario. The observed results consistently align with the theoretical time complexities.

* Insertion: Tasks are inserted and the string representation shows how the heap structure adjusts by displaying the task’s id. Despite insertions,``` peekmax()``` always identifies the highest priority task. It demonstrates the <em>O(</em>log <em>n)</em> efficiency of insert in maintaining the heap property.
* Extraction: Calls to ``` extractmax()``` remove tasks in decreasing order of priority. Each extraction is visibly fast, which shows its <em>O(</em>log <em>n)</em> time complexity. The heap dynamically readjusts after each removal, ensuring the next highest priority task is always at the root.
* Modification: Modifications update the task priorities quickly. When Task "T001" (priority 4) is increased to 9, it bubbled up and became the new highest priority task. This demonstration highlighted the  <em>O(</em>log <em>n)</em> efficiency of` ``` _heapify_incr ``` method. In the differing operation, when "T003" (priority 7) decreased to 0, it bubbled down. This showcased ```_heapify_desc``` in a similar fashion. The dynamic adjustments are critical for real-world scheduling where task priorities can rapidly change.

The empirical results from this application confirmed the time complexities of the core operations for the Priority Queue.

## References
Chen, F., Chen, N., Mao, H., and Hu, H. (2018). <em>An efficient sorting algorithm - Ultimate Heapsort(UHS)</em>. https://doi.org/10.48550/arxiv.1902.00257

Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. (2022). Introduction to Algorithms<em>, 4th edition.</em> Cambridge. The MIT Press.





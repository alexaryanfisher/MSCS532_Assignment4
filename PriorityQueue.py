"""
Assignment 4: Part A.

Priority Queue Implementation

"""

import time

# Create class called Task to represent task managed by Priority Queue.
class Task:
    # Define attributes.
    def __init__ (self, task_id, priority, arrival_time, deadline, description=""):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.description = description
        # Initialize with -1 to be updated by PriorityQueue
        self._index_inheap = -1

    def __lt__(self, other):
        # Define less than comparsion for Task objects, to be used by heap to determine priority order.
        # Max heap, tasks with higher priority to be considered larger.

        if self.priority != other.priority:
            return self.priority < other.priority
        # To resolve tie-breakers.
        return self.task_id < other.task_id
    
    def __str_rep__(self):
        # String representation for display and debugging.
        return (f"Task( ID: '{self.task_id}', Priority: {self.priority}, "
                f"Arrival: {self.arrival_time:.2f}, Deadline: {self.deadline:.2f}, Description: '{self.description}')")
    
# Priority Queue Class. Implements Max-Priority Queue using a arrat as a binary heap. Highest priority tasks are extracted first.
class PriorityQueue:
    def __init__(self):
        # List representing the heap.
        self._heap = []
        # Map task id to its index in the heap for <em>O</em>(1) searching.
        self._taskid_toindex = {}
    
    # Retrieve Parent Index
    def _get_parentindex(self, i):
        return (i -1) // 2
    
    # Retrieve left child Index
    def _get_leftchild(self, i):
        return 2 * i + 1
    
    # Retrieve right child Index
    def _get_righttchild(self, i):
        return 2 * i + 2
    
    # Swap with the use of a helper to swap two elements in the heap and update their index in heap mapping.
    def _swap(self, i, j):
        i_task = self._heap[i]
        j_task = self._heap[j]

        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

        # Update the internal index.
        i_task._index_inheap = j
        j_task._index_inheap = i

        # Update dictionary mapping for task id to current index.
        self._taskid_toindex[i_task.task_id] = j
        self._taskid_toindex[j_task.task_id] = i
    
    # Restores max heap property by bubbling up element at index i. Used after insertion or increasing key priority.
    def _heapify_incr(self, i):
        while i > 0 and self._heap[self._get_parentindex(i)] < self._heap[i]:
            parentindex = self._get_parentindex(i)
            self._swap(i,parentindex)
            i = parentindex

    # Restores max heap property by bubbling down element at index i. Used after extraction of max or decreasing key priority.
    def _heapify_desc(self, i):
        n = len(self._heap)
        # Intialize largest as root
        largest = i
        # Get index of left child of root.
        l = self._get_leftchild(i)
        # Get index of left child of root
        r = self._get_righttchild(i)

        # If left child exists and is greater than root. Set the largest to left child.
        if l < n and self._heap[l] > self._heap[largest]:
            largest = l
        
        # If right child exists and is greater than the current largest. Set the largest to right child.
        if r < n and self._heap[r] > self._heap[largest]:
            largest = r
        
        # If largest is not equal to root, swap index with largest and continue heapifying current largest.
        if largest != i:
            self._swap(i, largest)
            self._heapify_desc(largest)

    # Core Operations of application.

    # Insert new task.
    def insert(self, task):
        # Error checking to see if task id exists.
        if task.task_id in self._taskid_toindex:
            print(f"Task with Task ID '{task.task_id}' already exists. To modify use Modify_priority to update.")
            return
        
        self._heap.append(task)
        newindex = len(self._heap) - 1
        # Store index into the task object.
        task._index_inheap = newindex
        # Map task id to index.
        self._taskid_toindex[task.task_id] = newindex

        # Restore heap property.
        self._heapify_incr(newindex)

    # Extract Max, Removes the highest priority (root)
    def extractmax(self):
        if len(self._heap) == 1:
            maxtask = self._heap.pop()
            del self._taskid_toindex[maxtask.task_id]
            maxtask._index_inheap = -1
            return maxtask
        
        maxtask = self._heap[0]
        # Move last element to root.
        self._swap(0, len(self._heap) - 1)
        # Remove old root.
        self. _heap.pop()
        # Remove from map.
        del self._taskid_toindex[maxtask.task_id]
        # Note as no longer in the heap.
        maxtask._index_inheap = -1

        # Restore heap propert from new root.
        self._heapify_desc(0)

        return maxtask


    # Modify Priority of existing task and adjust its position.
    def modify(self, task_id, new_priority):
    
        index = self._taskid_toindex[task_id]
        task = self._heap[index]
        old_priority = task.priority

        # If priority stays the same.
        if new_priority == old_priority:
            print(f"Priority of Task '{task_id}' is already the same {new_priority} priority. No change needed.")
            return False
        
        task.priority = new_priority

        # If priority decreases.
        if new_priority < old_priority:
            self._heapify_desc(index)
            print(f"Priority of Task '{task_id}' has decreased from {old_priority} to {new_priority}")
        else:
            # If priority increases.
            self._heapify_incr(index)
            print(f"Priority of Task '{task_id}' has increased from {old_priority} to {new_priority}")
        return True

    # Check if Priority Queue is empty.
    def isempty(self):
        return len(self._heap) == 0
    
    # Display highest priority without removing it.
    def peekmax(self):
        if self.isempty():
            return None
        # Return Task ID.
        return self._heap[0].task_id

    # Return number of tasks currently in priority queue.
    def __len__(self):
        return len(self._heap)
    
    # String representation of heap for debugging.
    def __str__(self):
        return f"Heap Size (size {len(self._heap)}): {[t.task_id for t in self._heap]}"
    

# Use Cases
if __name__ == "__main__":
    print("Priority Queue Demo (Max Heap)")
    pq = PriorityQueue()

    # Create some tasks to show examples.
    task1 = Task("T001", 4, time.time(), time.time() + 3600, "High Priority Bug Fix")
    task2 = Task("T002", 1, time.time() + 25, time.time() + 7200, "Maintenance")
    task3 = Task("T003", 7, time.time() + 5, time.time() + 1600, "Feature Enhancement")
    task4 = Task("T004", 8, time.time() + 20, time.time() + 800, "Critical Update: Security Patch")
    task5 = Task("T005", 4, time.time() + 15, time.time() + 2200, "Document Update")

    # Insertion of Tasks.
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    pq.insert(task4)
    pq.insert(task5)
    print(f"Current Priority Queue: {pq}")
    print(f"Show Highest priority task: {pq.peekmax()}")

    # Extracting Max Priority Task.
    highest_prioritytask = pq.extractmax()
    if highest_prioritytask:
            print(f"Extracted Task ID: {highest_prioritytask.task_id}")
    print(f"Priority Queue after extraction: {pq}")
    print(f"Show current highest priority task: {pq.peekmax()}")

    # Updating Priority, increasing
    print(f"Before priority update for T001: {pq}")
    # Make it very high priority
    pq.modify("T001", 9) 
    # Show new priorities
    print(f"After priority update for T001: {pq}")
    print(f"Show current highest priority task: {pq.peekmax()}")

    # Updating Priority, decreasing
    print(f"Before priority update for T003: {pq}")
    # Make it very low priority
    pq.modify("T003", 0) 
    # Show new priorities
    print(f"After priority update for T003: {pq}")
    print(f"Show current highest priority task: {pq.peekmax()}")

    # Extracting Remaining Tasks and check to see if priority queue is empty.
    while not pq.isempty():
        task = pq.extractmax()
        print(f"Extracted: {task.task_id}")
    print(f"Priority Queue after all extractions: {pq}")
    print(f"Is priority queue empty?: {pq.isempty()}")
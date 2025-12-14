
# Queue Structures

A **queue** is a fundamental data structure that follows the **First In, First Out (FIFO)** principle, meaning the first element added is the first one to be removed.

Queues can be implemented using arrays or linked lists. In a linked-list-based queue, each element is stored in a **node**, with references to the next node, and the queue maintains pointers to both the **front** and **rear** nodes. This enables dynamic growth and shrinkage efficiently.

### Key Operations
- `enqueue(element)`: Adds an element to the rear of the queue.
- `dequeue()`: Removes and returns the element from the front of the queue.
- `peek()`: Returns the front element without removing it.
- `is_empty()`: Checks whether the queue is empty.

Queues are widely used in:
- Task scheduling and process management
- Breadth-first search (BFS) in graph algorithms
- Buffer management in data streaming and network communication


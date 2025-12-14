# Stack Structures

A **stack** is a fundamental data structure that follows the **Last In, First Out (LIFO)** principle, meaning the last element added is the first one to be removed.

Stacks can be implemented using arrays or linked lists. In a linked-list-based stack, each element is stored in a **node**, where each node contains the data and a reference to the next node. This allows the stack to grow and shrink dynamically without worrying about fixed capacity.

### Key Operations
- `push(element)`: Adds an element to the top of the stack.
- `pop()`: Removes and returns the top element from the stack.
- `peek()`: Returns the top element without removing it.
- `is_empty()`: Checks whether the stack is empty.

Stacks are widely used in:
- Expression evaluation (e.g., arithmetic expressions, postfix notation)
- Backtracking algorithms (e.g., maze solving, N-Queens)
- Function call management (call stack in programming languages)

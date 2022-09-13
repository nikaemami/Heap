# Heap
Implementation a program using a **min heap** to return the **minimum number** an action needs to be done.

<h2>Chain_Linkage:</h2>

For connecting two chains with lengths l and k, we need to flip l+k times. What is the **minimum count** of flips for connecting n chains together?

INPUT: In the first line n is given as the **number of chains**. In the next line n numbers are given, each indicating the **length of the corresponding chain**.

OUTPUT: In the only line of output, print the minimum number of flips.

**INPUT:**

5

3 5 1 4 2

**OUTPUT:**

33

First, a class minHeap is defined, which consists the right and left children, and the parent of each node:

```ruby
class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
 
    def parent(self, position):
        return (position//2)
 
    def leftChild(self, position):
        return 2 * position

    def rightChild(self, position):
        return (2 * position) + 1
```

Next, some functions for basic operations in a heap, like **swap** and **insert** are implemented:

```ruby
swap(root, position1, position2)
def insert(root, element)
```
Next, a **Heapify** function is implemented, which is what actually creates the heap. The key part of the minHeapify function:

```ruby
if root.Heap[root.leftChild(node)] >= root.Heap[root.rightChild(node)]:
  swap(root, node, root.rightChild(node))
  minHeapify(root,root.rightChild(node))
else:
  swap(root, node, root.leftChild(node))
  minHeapify(root,root.leftChild(node))
```

Finally, the summation that computes the output, is calculated by getting the root of the heap multiple times, to get the smallest values in order:

```ruby
popped_2 = root.Heap[root.leftChild(root.FRONT)]
popped_1 = root.Heap[root.FRONT]
sum+= popped_1 + popped_2 + popped_1 + root.Heap[root.leftChild(root.FRONT)] + root.Heap[root.rightChild(root.FRONT)]
```

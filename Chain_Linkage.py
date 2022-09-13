import sys
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

def swap(root, position1, position2):
        temp = root.Heap[position1]
        root.Heap[position1] = root.Heap[position2]
        root.Heap[position2] = temp

def insert(root, element):
    if root.size >= root.maxsize :
        return
    root.size+= 1
    root.Heap[root.size] = element
    
    current = root.size
 
    while root.Heap[current] < root.Heap[root.parent(current)]:
        swap(root, current, root.parent(current))
        current = root.parent(current)

def Leaf(root, node):
    return node*2 > root.size

def minHeapify(root, node):
    condition = Leaf(root,node)
    if (condition == 0):
        if ((root.Heap[node] > root.Heap[root.leftChild(node)]) or (root.Heap[node] > root.Heap[root.rightChild(node)])):
 
            if root.Heap[root.leftChild(node)] >= root.Heap[root.rightChild(node)]:
                swap(root, node, root.rightChild(node))
                minHeapify(root,root.rightChild(node))
            else:
                swap(root, node, root.leftChild(node))
                minHeapify(root,root.leftChild(node))
                    
def minHeap(root):
        for node in range(root.size//2, 0, -1):
            minHeapify(root,node)

n = int(input())
chains = list(map(int,input().split()))
root = MinHeap(n)
for i in (chains):
    insert(root,i)
minHeap(root,root.FRONT)

sum = 0
while (root.size >= 2):

    if (root.Heap[root.leftChild(root.FRONT)] <= root.Heap[root.rightChild(root.FRONT)]):
        popped_2 = root.Heap[root.leftChild(root.FRONT)]
        popped_1 = root.Heap[root.FRONT]
        root.Heap[root.FRONT] = root.Heap[root.size]
        root.size-= 1
        if (root.size > 3):
            root.Heap[root.leftChild(root.FRONT)] = root.Heap[root.size]
            root.size-= 1
        else:
            sum+= popped_1 + popped_2   
            root.Heap[root.leftChild(root.FRONT)] = popped_1 + popped_2
            minHeapify(root,root.FRONT)
            popped_1 = root.Heap[root.FRONT]
            if (root.Heap[root.leftChild(root.FRONT)] <= root.Heap[root.rightChild(root.FRONT)]):
                popped_2 = root.Heap[root.leftChild(root.FRONT)]
            else:
                popped_2 = root.Heap[root.rightChild(root.FRONT)]
            sum+= popped_1 + popped_2 + popped_1 + root.Heap[root.leftChild(root.FRONT)] + root.Heap[root.rightChild(root.FRONT)]
            break
        
    else:
        popped_2 = root.Heap[root.rightChild(root.FRONT)]
        popped_1 = root.Heap[root.FRONT]
        root.Heap[root.FRONT] = root.Heap[root.size]
        root.size-= 1
        if (root.size > 3):
            root.Heap[root.rightChild(root.FRONT)] = root.Heap[root.size]
            root.size-= 1
        else:
            sum+= popped_1 + popped_2   
            root.Heap[root.rightChild(root.FRONT)] = popped_1 + popped_2
            minHeapify(root,root.FRONT)
            popped_1 = root.Heap[root.FRONT]
            if (root.Heap[root.leftChild(root.FRONT)] <= root.Heap[root.rightChild(root.FRONT)]):
                popped_2 = root.Heap[root.leftChild(root.FRONT)]
            else:
                popped_2 = root.Heap[root.rightChild(root.FRONT)]
            sum+= popped_1 + popped_2 + popped_1 + root.Heap[root.leftChild(root.FRONT)] + root.Heap[root.rightChild(root.FRONT)]
            break


    if (root.size >= 3):
        minHeapify(root,root.FRONT)
        sum+= popped_1 + popped_2   
        insert(root, (popped_1 + popped_2))

print(sum)
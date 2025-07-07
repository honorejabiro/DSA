# Given a Binary Tree, the task is to find its Level Order Traversal.
# Finding the parent arr[(i-1) / 2], left child arr[(i*2) + 1] and lastly for right child arr[(i*2) + 2]

# Implementation of our Heap class
from collections import deque
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Using Recursion
def level_order_rec(root, level, res):

    if root is None:
        return None
    
    if len(res) <= level:
        res.append([])

    res[level].append(root.data)

    level_order_rec(root.left, level+1, res)
    level_order_rec(root.right, level+1, res)

# Using Queue
def level_order_queue(root):
    if root is None:
        return None
    
    res = []
    # Create the res list
    # Create the Queue
    queue = deque()
    # Add the node in the queue
    queue.append(root)
    # While queue
    while queue:
        # Get the length of the queue
        length = len(queue)
        # Iterate in length of the queue
        # Define array for current level
        arr = []
        for i in range(length):
            # Pop from the queue
            node = queue.popleft()
            # Add the temp array
            arr.append(node.data)
            # add its children if availble
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(arr)

    return res

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    res = level_order_queue(root)
    res1 = []
    level_order_rec(root, 0, res1)

    for level in res:
        print([f"{', '.join(map(str, level))}"], end='')
    print('\n')

    for level in res1:
        print([f"{', '.join(map(str, level))}"], end='')
    print('\n')

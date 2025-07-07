# In Heap Sort, we use Binary Heap so that we can quickly find and move the max element in O(Log n) instead of O(n) and hence achieve the O(n Log n) time complexity.

# Pseudocode
# Rearage the array elements so that they form a Max Heap. Using Heapify
# Repeat the following steps until the heap contains only one element:
    # Swap the root element with the last element
    # Remove the last element which is now the largest element
    # Heapify the rest of the heap
# Finally we get the sorted array

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def heapify(arr, n, i):

    # Initialize largest as root
    largest = i
    # left index for heap is (2*i) + 1
    l = (2*i) + 1

    # Right index for heap is (2*i) + 2
    r = (2*i) + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If the largest index with largest number is not in the root swap
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # you swap here

        # Reculsively heapiy the affected sub-tree
        heapify(arr, n, largest)

# Main function to do heap sort
def heapSort(arr):

    n = len(arr)

    # Build the heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by ine exract an element from heap
    for i in range(n-1, 0, -1):
        
        # Move the top element to the 
        arr[i], arr[0] = arr[0], arr[i]

        # Call the max heapify
        heapify(arr, i, 0)

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver's code
arr = [9, 4, 3, 8, 10, 2, 5] 
heapSort(arr)
print("Sorted array is ")
printArray(arr)
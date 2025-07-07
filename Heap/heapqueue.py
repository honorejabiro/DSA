# A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap) or largest (max-heap) element.
# In python Heaps are represented as Min Heap as default.

import heapq

# Creating a basic priority queue
li = [10, 20, 15, 30, 40]

heapq.heapify(li)

print("Heap queue:", li)

# Key operations:
    # Push (heappush): Adds an element to the heap while maintaining the heap property.
    # Pop (heappop): Removes and returns the smallest element in the heap, again maintaining the heap property.
    # Peek: View the smallest element without removing it.
    # Heapify: Convert a regular list into a valid heap in-place.

# Push operation
heapq.heappush(li, 60)
print("Heap queue with 60 pushed in:", li)

# Pop operation
minimum = heapq.heappop(li)
print("Minimum:", minimum)
print(li)

# Appending and popping simultaneously
mini = heapq.heappushpop(li, 25)
print(mini)
print(li)

# Finding nlargest and nsmallest
# Returns an array of n lrgest or n smallest numbers
mini = heapq.nsmallest(3, li)
maxi = heapq.nlargest(3, li)
print("the list: ", li)
print("the min: ", mini)
print("the max: ", maxi)

# Replace and Merge Operation
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)

# This replaces the smallest element with 5
mini = heapq.heapreplace(h1, 5)

# Merging Heaps
h2 = [2, 4, 6, 8]

# Merging the lists
h3 = list(heapq.merge(h1, h2))
print("Merged heap:", h3)
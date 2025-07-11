import heapq
def lastStoneWeight(stones) -> int:
    # Create a max heap
    # Repeat this process until the array has 1 element
        # pop the top element
        # pop the second element
        # find the difference
        # if difference is greater than 1 add it to the list
    # Return the last element in he list

    # Function to make elements negative to make the heap a max heap
    def max_heap(li):
        for i in range(len(li)):
            li[i] = li[i] * -1
    
    max_heap(stones)
    heapq.heapify(stones)
    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        diff = (y*-1) - (x*-1)
        if diff > 0:
            heapq.heappush(stones, (diff*-1))
    if stones:
        return (stones[0] * -1)
    return 0

def main():
    stones = [2,7,4,1,8,1]
    print(lastStoneWeight(stones))

if __name__ == "__main__":
    main()

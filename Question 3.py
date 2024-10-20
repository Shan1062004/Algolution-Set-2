import heapq

def find_kth_largest(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return heapq.heappop(min_heap)


nums = [3, 2, 1, 5, 6, 4]
k = 2
print("The", k, "th largest element is:", find_kth_largest(nums, k))

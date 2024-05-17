class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return kth largest element
        # use minHeap and maintain k elements inside the heap
        # so the root will be the smallest of k elements, therefore the kth largest

        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
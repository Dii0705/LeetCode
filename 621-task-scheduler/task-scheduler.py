class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # identical tasks must be separated by at least n intervals
        # return the min number of intervals required

        # hint: find the most frequent letter for every circle, place it, decrease the frequency by one

        # find the most frequent letter
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        wait_queue = deque() # pairs of [-count, idleTime]
        time = 0

        while maxHeap or wait_queue:
            time += 1
            
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1 # add 1 because we store maxHeap element as negative
                if count:
                    wait_queue.append([count, time + n])
                
            if wait_queue and wait_queue[0][1] == time:  # if idleTime has passed
                heapq.heappush(maxHeap, wait_queue.popleft()[0]) # add back to heap for processes
        return time

        

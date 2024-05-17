class Twitter:

    def __init__(self):
        self.tracker = 0
        self.tweetMap = defaultdict(list) # userId -> list of [tracker, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.tracker, tweetId])
        self.tracker -= 1 # since we use minHeap, the smaller the tracker, the most recent 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from the recent
        minHeap = []

        self.followMap[userId].add(userId) # don't forget to add the user themselves
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) -1
                tracker, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([tracker, tweetId, followeeId, index -1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            tracker, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                tracker, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [tracker, tweetId, followeeId, index -1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
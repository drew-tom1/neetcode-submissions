class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush_max(self.tweets[userId], (self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = list(self.tweets[userId])
        for follower in self.followers[userId]:
            candidates.extend(self.tweets[follower])
        heapq.heapify_max(candidates)
        res = []
        
        while candidates and len(res) < 10:
            _, tweet = heapq.heappop_max(candidates)
            res.append(tweet)
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
        

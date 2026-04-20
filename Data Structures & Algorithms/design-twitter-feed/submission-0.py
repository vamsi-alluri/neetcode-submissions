from heapq import heappush, heappop
class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        # Adding user's tweets.
        for time, tweetId in self.tweet_map[userId]:
            heappush(feed, (-time, tweetId)) # Max heap
        
        for followeeUserId in self.follow_map[userId]:
            for time, tweetId in self.tweet_map[followeeUserId]:
                heappush(feed, (-time, tweetId)) # Max heap
        
        res = []

        i = 0
        while feed and i < 10:
            res.append(heappop(feed)[1]) # store the tweet ids, pops the recent first.
            i += 1
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].discard(followeeId)

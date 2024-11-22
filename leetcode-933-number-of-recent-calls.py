# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.requests = []
        self.lastInRange = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while t - self.requests[self.lastInRange] > 3000:
            self.lastInRange += 1  

        return len(self.requests) - self.lastInRange

# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        avg = sum(nums[:k])/k
        maxAvg = avg

        for i in range(k, len(nums)):
            avg += (nums[i] - nums[i - k])/k

            maxAvg = max(maxAvg, avg)
    
        return maxAvg
            

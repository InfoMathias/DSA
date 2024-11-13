# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1

        for right in range(len(nums)):
            k += nums[right] - 1
            
            if k < 0:
                k += 1 - nums[left]
                left += 1        

        return right - left

# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k += nums[right] - 1

            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1

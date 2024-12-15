# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]

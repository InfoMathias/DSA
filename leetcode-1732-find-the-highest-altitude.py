// https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        gain = [0] + gain
        maxGain = gain[0]

        for i in range(1, len(gain)):
            gain[i] = gain[i-1] + gain[i]
            maxGain = max(maxGain, gain[i])

        return maxGain

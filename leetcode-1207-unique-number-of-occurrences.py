# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}

        for num in arr:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1

        counts = set()

        for key in occurences:
            if occurences[key] in counts:
                return False
            else:
                counts.add(occurences[key])

        return True

# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = {}
        
        for row in grid:
            row_counts[tuple(row)] = row_counts.get(tuple(row),0) + 1
        
        counter = 0
        
        n = len(grid)
        for j in range(n):
            col_tuple = tuple(grid[i][j] for i in range(n))
            if col_tuple in row_counts:
                counter += row_counts[col_tuple]
        
        return counter

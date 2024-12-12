# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = collections.deque([[entrance[0], entrance[1], 0]])

        while queue:
            x, y, count = queue.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            if (x==0 or y==0 or x==m-1 or y==n-1) and (x!=entrance[0] or y!=entrance[1]):
                return count
            if x+1<m and maze[x+1][y]==".":
                queue.append([x+1, y, count+1])
            if x-1>=0 and maze[x-1][y]==".":
                queue.append([x-1, y, count+1])
            if y+1<n and maze[x][y+1]==".":
                queue.append([x, y+1, count+1])
            if y-1>=0 and maze[x][y-1]==".":
                queue.append([x, y-1, count+1])

        return -1

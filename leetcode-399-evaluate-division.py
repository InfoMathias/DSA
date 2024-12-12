# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # map {a: [[b, 2], [c, 1]]}
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def dfs(start, target, accW, visited):
            if start not in adj or target not in adj or start in visited:
                return -1
            if start == target:
                return accW
            visited.add(start)
            for n, w in adj[start]:
                res = dfs(n, target, accW*w, visited)
                if res != -1:
                    return res
            return res

        return [dfs(q[0], q[1], 1, set()) for q in queries]

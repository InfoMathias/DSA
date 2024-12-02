# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.maxCount = 0
        def dfs(node, count, left):
            self.maxCount = max(self.maxCount, count)
            if node.left:
                dfs(node.left, count + 1, True) if not left else dfs(node.left, 1, True)
            if node.right:        
                dfs(node.right, count + 1, False) if left else dfs(node.right, 1, False) 

        if root.left:
            dfs(root, 0, True)
        else: 
            dfs(root, 0, False)

        return self.maxCount


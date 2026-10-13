# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: TreeNode, maxVal: int):
            if node.val >= maxVal:
                nonlocal res
                res += 1
            
            if node.left:
                dfs(node.left, max(node.val, maxVal))
            
            if node.right:
                dfs(node.right, max(node.val, maxVal))
        
        dfs(root, -101)
        
        return res

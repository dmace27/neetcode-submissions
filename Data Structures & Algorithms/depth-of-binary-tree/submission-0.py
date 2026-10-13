# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxd = 1
        stack = []
        sd = {}
        stack.append(root)
        sd[root] = 1

        
        while stack:
            x = stack[-1]
            stack.pop()
            if x.right:
                stack.append(x.right)
                sd[x.right] = sd[x] + 1
            if x.left:
                stack.append(x.left)
                sd[x.left] = sd[x] + 1
            
            if sd[x] > maxd:
                maxd = sd[x]
        
        return maxd
            
            
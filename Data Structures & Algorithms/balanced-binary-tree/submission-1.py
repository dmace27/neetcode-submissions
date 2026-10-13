# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            return 1 + max(l, r)
        
        if not root:
            return True
        dif = dfs(root.right) - dfs(root.left)
        if dif > 1 or dif < -1:
            return False
        else:
            return True
        
        

        
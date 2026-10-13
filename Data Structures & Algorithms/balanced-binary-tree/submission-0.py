# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        r = 0
        l = 0
        if not root:
            return True

        def gd(node):
            if not node:
                return 0
            
            lh = gd(node.left)
            rh = gd(node.right)
            
            
            return max(lh, rh) + 1
    
        if not root.right:
            r = 0
        else:
            r = gd(root.right)
        if not root.left:
            l = 0
        else:
            l = gd(root.left)
        
        dif = l - r

        if dif < 2 and dif > -2:
            return True
        else:
            return False
        
        

        
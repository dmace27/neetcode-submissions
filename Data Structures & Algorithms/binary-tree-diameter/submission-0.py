# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = [0]
        if not root.right and not root.left:
            return 0
        

        def maxdepth(node: Optional[Treenode]):
            
            if not node:
                return 0
            
            lh = maxdepth(node.left)
        
            rh = maxdepth(node.right)

            maxd[0] = max(maxd[0], lh+rh)
        
            return max(lh, rh)+1
        
        maxdepth(root)

        return maxd[0]
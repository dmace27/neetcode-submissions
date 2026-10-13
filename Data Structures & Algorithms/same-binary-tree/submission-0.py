# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        
        
        q1 = []
        q1.append(q)
        q2 = []
        q2.append(p)
        while q1:
            c1 = q1[-1]
            q1.pop()
            c2 = q2[-1]
            q2.pop()

            if c1.val != c2.val:
                return False
            
            if c1.right:
                q1.append(c1.right)
            if c2.right:
                q2.append(c2.right)
            
            if len(q1) != len(q2):
                return False

            if c1.left:
                q1.append(c1.left)
            if c2.left:
                q2.append(c2.left)
            

            if len(q1) != len(q2):
                return False

        return True
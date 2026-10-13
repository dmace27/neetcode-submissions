# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = []
        p  = 0

        if root:
            q.append(root)
        else:
            return root
        while q:
            curr = q[p]

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            
            # in the case the node has both children
            dummy = curr.right
            curr.right = curr.left
            curr.left = dummy

            q.remove(q[p])
        
        return root
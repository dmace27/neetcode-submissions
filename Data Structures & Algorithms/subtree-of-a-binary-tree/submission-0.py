# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        q = []
        q.append(root)

        def check(p: TreeNode, q: TreeNode) -> bool:
            if p and q:
                if p.val != q.val:
                    return False
            elif not p and not q:
                return True
            else:
                return False
            
            
            s1 = []
            s1.append(q)
            s2 = []
            s2.append(p)
            while s1:
                c1 = s1[-1]
                s1.pop()
                c2 = s2[-1]
                s2.pop()

                if c1.val != c2.val:
                    return False
                
                if c1.right:
                    s1.append(c1.right)
                if c2.right:
                    s2.append(c2.right)
                
                if len(s1) != len(s2):
                    return False

                if c1.left:
                    s1.append(c1.left)
                if c2.left:
                    s2.append(c2.left)
                

                if len(s1) != len(s2):
                    return False

            return True




        while q:
            curr = q[0]
            q.pop(0)
            if curr.val == subRoot.val:
                if check(curr, subRoot):
                    return True
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        

        return False
        
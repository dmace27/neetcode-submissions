# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
              
        l, h, ch, q = [], {}, 0, []
        
        if root:
            q.append(root)
            h[root] = ch
        else:
            return l

        while q:
            curr = q[0]
            q.pop(0)
            ch = h[curr]

            if curr.right:
                q.append(curr.right)
                h[curr.right] = ch + 1
            
            if curr.left: 
                q.append(curr.left)
                h[curr.left] = ch + 1
                
            # adding the node to the nested list
            if len(l) <= ch:
                l.append([])
            
            l[ch].insert(0,curr.val)
        
        return l
    
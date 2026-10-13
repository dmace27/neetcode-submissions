# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def search(root: TreeNode, node: TreeNode) -> List[TreeNode]:
            curr = root
            ancestors = []
            while True:
                ancestors.append(curr)
                if curr.val == node.val:
                    break
                elif curr.val > node.val:
                    curr = curr.left
                else:
                    curr = curr.right
            return ancestors
        
        if p.val == root.val or q.val == root.val:
            return root
      
        pa = search(root, p)
        qa = search(root, q)

        lca = root
        for i in range(min(len(pa), len(qa))):
            if qa[i] and pa[i].val == qa[i].val:
                lca = pa[i]
        
        return lca
        